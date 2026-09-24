from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "catalog.py"
SPEC = importlib.util.spec_from_file_location("catalog", SCRIPT)
catalog = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(catalog)


def paper(paper_id="P01", identifier="10.1234/example"):
    return {
        "id": paper_id,
        "title": f"Title {paper_id}",
        "authors_display": "A. Author; B. Author",
        "year": 2024,
        "venue_version": "Example v1",
        "identifier": identifier,
        "url": "https://example.org/paper/" + paper_id,
        "branch": "基礎",
        "role": "原理",
        "prerequisites": [],
        "reason_to_read": "読む理由",
        "reading_question": "読む問い",
        "marginal_value": "追加価値",
        "limitations": "限界",
        "evidence_depth": "要旨確認",
        "evidence_url": "https://example.org/evidence/" + paper_id,
        "evidence_locator": "Abstract",
        "status": "候補・要旨のみ確認",
        "discovery_route": "検索",
        "queue": "導入",
    }


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.write([paper()], [])

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, papers, relations):
        payload = {"schema_version": 9, "release": "test", "scope": "fixture", "papers": papers}
        (self.root / "papers.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        (self.root / "relations.json").write_text(json.dumps(relations, ensure_ascii=False), encoding="utf-8")

    def assert_invalid(self, fragment):
        with self.assertRaisesRegex(catalog.CatalogError, fragment):
            catalog.validate(self.root)

    def test_reading_question_precedes_bibliographic_metadata(self):
        for card in (True, False):
            text = "\n".join(catalog._paper_lines(paper(), card=card))
            self.assertLess(text.index("- 読む問い："), text.index("- 著者："))

    def test_identical_selection_explanations_are_not_repeated(self):
        p = paper()
        p["selection"] = {"decision": "維持", "importance": p["reason_to_read"],
                          "alternative": p["marginal_value"], "confidence": "編集判断"}
        text = "\n".join(catalog._paper_lines(p, card=True))
        self.assertNotIn("- 役割：", text)
        self.assertNotIn("- 重要性：", text)
        self.assertNotIn("- 選定上の補完性・代替との関係：", text)
        self.assertIn("- 選定判断：維持", text)
        self.assertIn("- 確信度：編集判断", text)

    def test_distinct_selection_explanations_are_preserved(self):
        p = paper()
        p["selection"] = {"decision": "維持", "importance": "歴史的位置付け",
                          "alternative": "別教材との比較", "confidence": "編集判断"}
        text = "\n".join(catalog._paper_lines(p, card=True))
        self.assertIn("- 重要性：歴史的位置付け", text)
        self.assertIn("- 選定上の補完性・代替との関係：別教材との比較", text)
        self.assertIn("- 限界・注意：限界", text)
        self.assertIn("- 根拠の確認範囲：要旨確認", text)

    def test_valid_roundtrip_is_byte_deterministic_and_check_is_read_only(self):
        first = paper()
        first["required_background"] = ["確率論"]
        first["evidence_claims"] = [{
            "claim": "個別主張", "url": "https://example.org/claim",
            "locator": "§2", "depth": "本文確認", "ignored_extra": True,
        }]
        first["selection"] = {
            "decision": "採用", "importance": "高", "alternative": "なし", "confidence": "中",
        }
        second = paper("P02", "arXiv:2401.12345v2")
        second["prerequisites"] = ["P01"]
        relations = [
            {"from": "P02", "to": "P01", "type": "cites", "meaning": "引用",
             "evidence_url": "https://example.org/source", "evidence_locator": "References", "quote": "entry"},
            {"from": "P01", "to": "P02", "type": "recommended_before", "meaning": "推奨"},
            {"from": "P01", "to": "P02", "type": "compare", "meaning": "比較"},
        ]
        self.write([first, second], relations)

        command = [sys.executable, str(SCRIPT), "build", "--root", str(self.root)]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        paths = [self.root / "annotated-bibliography.md", self.root / "relations-view.md",
                 self.root / "papers/P01.md", self.root / "papers/P02.md"]
        before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "check", "--root", str(self.root)],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        after = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}
        self.assertEqual(before, after)

        expected = catalog._expected(self.root)
        catalog.build(self.root)
        self.assertEqual(expected, {path.relative_to(self.root): path.read_bytes() for path in paths})
        bibliography = paths[0].read_text(encoding="utf-8")
        self.assertIn("推奨学習順（必須依存ではない）", bibliography)
        self.assertIn("個別根拠", bibliography)
        self.assertIn("必要な背景知識：確率論", bibliography)

    def test_duplicate_id(self):
        self.write([paper(), paper()], [])
        self.assert_invalid("ID が重複")

    def test_duplicate_doi_with_url_and_case(self):
        self.write([paper(identifier="doi:10.1234/ABC"),
                    paper("P02", "https://doi.org/10.1234/abc")], [])
        self.assert_invalid("識別子.*重複")

    def test_duplicate_arxiv_ignores_version(self):
        self.write([paper(identifier="arXiv:2401.12345v1"),
                    paper("P02", "https://arxiv.org/abs/2401.12345v3")], [])
        self.assert_invalid("識別子.*重複")

    def test_missing_prerequisite(self):
        item = paper()
        item["prerequisites"] = ["P99"]
        self.write([item], [])
        self.assert_invalid("未定義の論文 ID: P99")

    def test_missing_edge_target(self):
        edge = {"from": "P01", "to": "P99", "type": "compare", "meaning": "比較"}
        self.write([paper()], [edge])
        self.assert_invalid("relations\\[0\\]\\.to: 未定義")

    def test_prerequisite_cycle(self):
        first, second = paper(), paper("P02", "10.1234/second")
        first["prerequisites"] = ["P02"]
        second["prerequisites"] = ["P01"]
        self.write([first, second], [])
        self.assert_invalid("循環")

    def test_malformed_evidence_claim(self):
        item = paper()
        item["evidence_claims"] = [{"claim": "x", "url": "file:///tmp/x", "locator": "", "depth": 1}]
        self.write([item], [])
        self.assert_invalid("evidence_claims")

    def test_malformed_types_are_reported_without_crashing(self):
        for field, value in [("id", []), ("prerequisites", None),
                             ("prerequisites", [{}]), ("url", "https://[bad")]:
            with self.subTest(field=field, value=value):
                item = paper()
                item[field] = value
                self.write([item], [])
                with self.assertRaises(catalog.CatalogError):
                    catalog.validate(self.root)
        self.write([paper()], [{"from": "P01", "to": "P01", "type": [], "meaning": "bad"}])
        with self.assertRaises(catalog.CatalogError):
            catalog.validate(self.root)

    def test_recommended_order_must_match_paper_metadata(self):
        first, second = paper(), paper("P02", "10.1234/second")
        second["prerequisites"] = ["P01"]
        self.write([first, second], [])
        self.assert_invalid("一致していません")

    def test_duplicate_relations_are_rejected(self):
        edge = {"from": "P01", "to": "P01", "type": "compare", "meaning": "test"}
        self.write([paper()], [edge, edge])
        self.assert_invalid("関係が重複")

    def test_generated_drift(self):
        catalog.build(self.root)
        target = self.root / "annotated-bibliography.md"
        target.write_text("changed\n", encoding="utf-8")
        with self.assertRaisesRegex(catalog.CatalogError, "差分"):
            catalog.check(self.root)

    def test_path_like_id_is_rejected_without_external_write(self):
        bad = paper("P01/../../escape", "10.1234/bad")
        self.write([bad], [])
        outside = self.root.parent / "escape.md"
        existed = outside.exists()
        self.assert_invalid("安全な ID")
        with self.assertRaises(catalog.CatalogError):
            catalog.build(self.root)
        self.assertEqual(outside.exists(), existed)

    def test_unexpected_card_stops_check_and_build_without_deleting_it(self):
        catalog.build(self.root)
        stray = self.root / "papers/P99.md"
        stray.write_text("manual?", encoding="utf-8")
        with self.assertRaisesRegex(catalog.CatalogError, "予期しない論文カード"):
            catalog.check(self.root)
        with self.assertRaisesRegex(catalog.CatalogError, "削除せず停止"):
            catalog.build(self.root)
        self.assertEqual(stray.read_text(encoding="utf-8"), "manual?")


if __name__ == "__main__":
    unittest.main()
