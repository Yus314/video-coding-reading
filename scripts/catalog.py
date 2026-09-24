#!/usr/bin/env python3
"""Validate catalog metadata and generate the repository's derived Markdown views."""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


PAPER_ID_RE = re.compile(r"^P[0-9]{2,}$")
ARXIV_RE = re.compile(
    r"^(?:arxiv:|https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/)"
    r"(?P<id>(?:[a-z-]+(?:\.[a-z]{2})?/\d{7}|\d{4}\.\d{4,5}))(?:v\d+)?(?:\.pdf)?/?$",
    re.IGNORECASE,
)
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
RELATION_TYPES = {"cites", "recommended_before", "compare"}
REQUIRED_TEXT_FIELDS = (
    "id", "title", "authors_display", "venue_version", "identifier", "url",
    "branch", "role", "reason_to_read", "reading_question", "marginal_value",
    "limitations", "evidence_depth", "evidence_url", "evidence_locator",
    "status", "discovery_route", "queue",
)
GENERATED_HEADER = "<!-- このファイルは scripts/catalog.py により自動生成されます。直接編集しないでください。 -->"


class CatalogError(Exception):
    """A user-facing validation or drift error."""


def _load_json(path: Path):
    try:
        with path.open(encoding="utf-8") as stream:
            return json.load(stream)
    except FileNotFoundError as exc:
        raise CatalogError(f"必須ファイルがありません: {path.name}") from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise CatalogError(f"{path.name} を読めません: {exc}") from exc


def _is_text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _http_url(value) -> bool:
    if not _is_text(value):
        return False
    if any(char.isspace() or char in "<>" for char in value):
        return False
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    return parsed.scheme.lower() in {"http", "https"} and bool(parsed.netloc)


def canonical_identifier(value: str) -> str:
    value = value.strip()
    arxiv = ARXIV_RE.fullmatch(value)
    if arxiv:
        return "arxiv:" + arxiv.group("id").lower()

    doi = re.sub(r"^(?:doi:\s*|https?://(?:dx\.)?doi\.org/)", "", value,
                 flags=re.IGNORECASE)
    if DOI_RE.fullmatch(doi):
        return "doi:" + doi.lower()

    try:
        parsed = urlsplit(value)
    except ValueError:
        return value.casefold()
    if parsed.scheme.lower() in {"http", "https"} and parsed.netloc:
        path = parsed.path.rstrip("/") or "/"
        return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path,
                           parsed.query, ""))
    return value.casefold()


def validate(root: Path):
    catalog = _load_json(root / "papers.json")
    relations = _load_json(root / "relations.json")
    errors: list[str] = []

    if not isinstance(catalog, dict):
        raise CatalogError("papers.json のトップレベルはオブジェクトである必要があります")
    papers = catalog.get("papers")
    if not isinstance(papers, list):
        raise CatalogError("papers.json の papers は配列である必要があります")
    if not isinstance(relations, list):
        raise CatalogError("relations.json のトップレベルは配列である必要があります")

    ids: dict[str, int] = {}
    identifiers: dict[str, str] = {}
    for index, paper in enumerate(papers):
        where = f"papers[{index}]"
        if not isinstance(paper, dict):
            errors.append(f"{where}: オブジェクトである必要があります")
            continue
        for field in REQUIRED_TEXT_FIELDS:
            if not _is_text(paper.get(field)):
                errors.append(f"{where}.{field}: 空でない文字列が必要です")
        paper_id = paper.get("id")
        if isinstance(paper_id, str):
            if not PAPER_ID_RE.fullmatch(paper_id):
                errors.append(f"{where}.id: 安全な ID (^P[0-9]{{2,}}$) ではありません: {paper_id!r}")
            elif paper_id in ids:
                errors.append(f"{where}.id: ID が重複しています: {paper_id}")
            else:
                ids[paper_id] = index
        if not isinstance(paper.get("year"), int) or isinstance(paper.get("year"), bool):
            errors.append(f"{where}.year: 整数が必要です")
        prerequisites = paper.get("prerequisites")
        if not isinstance(prerequisites, list) or not all(_is_text(x) for x in prerequisites):
            errors.append(f"{where}.prerequisites: 空でない文字列の配列が必要です")
        elif len(prerequisites) != len(set(prerequisites)):
            errors.append(f"{where}.prerequisites: 重複があります")
        for field in ("url", "evidence_url"):
            if field in paper and not _http_url(paper[field]):
                errors.append(f"{where}.{field}: http(s) URL が必要です")

        identifier = paper.get("identifier")
        if _is_text(identifier):
            canonical = canonical_identifier(identifier)
            if canonical in identifiers:
                errors.append(
                    f"{where}.identifier: 正規化後の識別子が {identifiers[canonical]} と重複しています: {identifier}"
                )
            else:
                identifiers[canonical] = str(paper_id or where)

        required_background = paper.get("required_background")
        if required_background is not None and (
            not isinstance(required_background, list)
            or not all(_is_text(x) for x in required_background)
        ):
            errors.append(f"{where}.required_background: 空でない文字列の配列が必要です")

        claims = paper.get("evidence_claims")
        if claims is not None:
            if not isinstance(claims, list):
                errors.append(f"{where}.evidence_claims: 配列が必要です")
            else:
                for claim_index, claim in enumerate(claims):
                    claim_where = f"{where}.evidence_claims[{claim_index}]"
                    if not isinstance(claim, dict):
                        errors.append(f"{claim_where}: オブジェクトが必要です")
                        continue
                    for field in ("claim", "url", "locator", "depth"):
                        if not _is_text(claim.get(field)):
                            errors.append(f"{claim_where}.{field}: 空でない文字列が必要です")
                    if "url" in claim and not _http_url(claim["url"]):
                        errors.append(f"{claim_where}.url: http(s) URL が必要です")

        selection = paper.get("selection")
        if selection is not None:
            if not isinstance(selection, dict):
                errors.append(f"{where}.selection: オブジェクトが必要です")
            else:
                for field in ("decision", "importance", "alternative", "confidence"):
                    if not _is_text(selection.get(field)):
                        errors.append(f"{where}.selection.{field}: 空でない文字列が必要です")

    known_ids = set(ids)
    graph = {paper_id: [] for paper_id in known_ids}
    for index, paper in enumerate(papers):
        if not isinstance(paper, dict) or not isinstance(paper.get("id"), str) or paper["id"] not in known_ids:
            continue
        prerequisites = paper.get("prerequisites")
        if not isinstance(prerequisites, list):
            continue
        for prerequisite in prerequisites:
            if not isinstance(prerequisite, str):
                continue
            if prerequisite not in known_ids:
                errors.append(f"papers[{index}].prerequisites: 未定義の論文 ID: {prerequisite}")
            else:
                graph[paper["id"]].append(prerequisite)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, trail: list[str]):
        if node in visiting:
            start = trail.index(node)
            errors.append("prerequisites: 循環があります: " + " -> ".join(trail[start:] + [node]))
            return
        if node in visited:
            return
        visiting.add(node)
        for neighbour in graph[node]:
            visit(neighbour, trail + [node])
        visiting.remove(node)
        visited.add(node)

    for paper_id in sorted(graph):
        visit(paper_id, [])

    for index, edge in enumerate(relations):
        where = f"relations[{index}]"
        if not isinstance(edge, dict):
            errors.append(f"{where}: オブジェクトが必要です")
            continue
        for field in ("from", "to", "type", "meaning"):
            if not _is_text(edge.get(field)):
                errors.append(f"{where}.{field}: 空でない文字列が必要です")
        for field in ("from", "to"):
            if _is_text(edge.get(field)) and edge[field] not in known_ids:
                errors.append(f"{where}.{field}: 未定義の論文 ID: {edge[field]}")
        if not isinstance(edge.get("type"), str) or edge["type"] not in RELATION_TYPES:
            errors.append(f"{where}.type: cites/recommended_before/compare のいずれかが必要です")
        if edge.get("type") == "cites":
            if not _http_url(edge.get("evidence_url")):
                errors.append(f"{where}.evidence_url: cites には http(s) URL が必要です")
            if not _is_text(edge.get("evidence_locator")):
                errors.append(f"{where}.evidence_locator: cites には空でない文字列が必要です")
            if "quote" in edge and not _is_text(edge["quote"]):
                errors.append(f"{where}.quote: 指定する場合は空でない文字列が必要です")

    if not errors:
        recommended = {(edge["from"], edge["to"]) for edge in relations
                       if edge["type"] == "recommended_before"}
        expected_order = {(previous, paper["id"]) for paper in papers
                          for previous in paper["prerequisites"]}
        if recommended != expected_order:
            errors.append("recommended_before と prerequisites が一致していません")
        keys = [(edge["from"], edge["to"], edge["type"]) for edge in relations]
        if len(keys) != len(set(keys)):
            errors.append("relations: 同じ関係が重複しています")
    if errors:
        raise CatalogError("データ検証に失敗しました:\n- " + "\n- ".join(errors))
    return catalog, papers, relations


def _text(value) -> str:
    """Keep generated Markdown list items on one line."""
    value = str(value).replace("\r", " ").replace("\n", " ").strip()
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def _link(label: str, target: str) -> str:
    return f"[{label}](<{target}>)"


def _paper_lines(paper: dict, *, card: bool) -> list[str]:
    prefix = "../papers/" if card else "papers/"
    prerequisites = paper["prerequisites"]
    prerequisite_text = (
        ", ".join(_link(item, prefix + item + ".md") for item in prerequisites)
        if prerequisites else "なし"
    )
    lines = [
        f"- 読む問い：{_text(paper['reading_question'])}",
        f"- 読む理由：{_text(paper['reason_to_read'])}",
        f"- 他の候補との差：{_text(paper['marginal_value'])}",
        f"- 著者：{_text(paper['authors_display'])}",
        f"- 年・版：{paper['year']} / {_text(paper['venue_version'])}",
        f"- 識別子：{_text(paper['identifier'])}",
        f"- 論文：{_link('公開ページ', paper['url'])}",
        f"- 分類：{_text(paper['branch'])} / {_text(paper['role'])} / {_text(paper['queue'])}",
        f"- 発見経路：{_text(paper['discovery_route'])}",
        f"- 推奨学習順（必須依存ではない）：{prerequisite_text}",
    ]
    if paper.get("required_background"):
        lines.append("- 必要な背景知識：" + ", ".join(_text(x) for x in paper["required_background"]))
    lines.extend([
        f"- 限界・注意：{_text(paper['limitations'])}",
        f"- 根拠の確認範囲：{_text(paper['evidence_depth'])} — {_text(paper['evidence_locator'])}",
        f"- 根拠資料：{_link('原文', paper['evidence_url'])}",
        f"- 読書状態：{_text(paper['status'])}",
    ])
    for claim in paper.get("evidence_claims", []):
        lines.append(
            f"- 個別根拠：{_text(claim['claim'])}（{_text(claim['depth'])}、"
            f"{_text(claim['locator'])}、{_link('原文', claim['url'])}）"
        )
    selection = paper.get("selection")
    if selection:
        lines.append(f"- 選定判断：{_text(selection['decision'])}")
        # Omit only identical rendered text; distinct editorial judgments remain.
        if _text(selection['importance']) != _text(paper['reason_to_read']):
            lines.append(f"- 重要性：{_text(selection['importance'])}")
        if _text(selection['alternative']) != _text(paper['marginal_value']):
            lines.append(f"- 選定上の補完性・代替との関係：{_text(selection['alternative'])}")
        lines.append(f"- 確信度：{_text(selection['confidence'])}")
    return lines


def render(catalog: dict, papers: list[dict], relations: list[dict]) -> dict[Path, bytes]:
    release = _text(catalog.get("release", "未指定"))
    scope = _text(catalog.get("scope", ""))
    bibliography = [GENERATED_HEADER, "", "# 注釈付き文献一覧", "",
                    f"リリース：{release}"]
    if scope:
        bibliography.extend(["", f"範囲：{scope}"])
    bibliography.extend(["", "`prerequisites` は必須依存関係ではなく、推奨学習順を表します。", ""])
    outputs: dict[Path, bytes] = {}
    for paper in papers:
        bibliography.extend([
            f"## {_link(paper['id'], 'papers/' + paper['id'] + '.md')} — {_text(paper['title'])}",
            "",
            *_paper_lines(paper, card=False),
            "",
        ])
        card_lines = [
            GENERATED_HEADER, "",
            f"# {paper['id']} — {_text(paper['title'])}", "",
            *_paper_lines(paper, card=True), "",
            f"関連ビュー：{_link('注釈付き文献一覧', '../annotated-bibliography.md')} / "
            f"{_link('関係一覧', '../relations-view.md')}", "",
        ]
        outputs[Path("papers") / f"{paper['id']}.md"] = ("\n".join(card_lines)).encode()
    outputs[Path("annotated-bibliography.md")] = ("\n".join(bibliography)).encode()

    relation_lines = [
        GENERATED_HEADER, "", "# 論文間の関係", "",
        "`recommended_before` は必須依存関係ではなく、推奨学習順です。引用や歴史的な先行関係を意味しません。", "",
    ]
    labels = {
        "cites": "引用（cites）",
        "recommended_before": "推奨学習順（recommended_before）",
        "compare": "比較（compare）",
    }
    for relation_type in ("cites", "recommended_before", "compare"):
        relation_lines.extend([f"## {labels[relation_type]}", ""])
        edges = [edge for edge in relations if edge["type"] == relation_type]
        if not edges:
            relation_lines.extend(["該当なし。", ""])
            continue
        for edge in edges:
            source = _link(edge["from"], f"papers/{edge['from']}.md")
            target = _link(edge["to"], f"papers/{edge['to']}.md")
            relation_lines.append(f"- {source} → {target}：{_text(edge['meaning'])}")
            if relation_type == "cites":
                relation_lines.append(
                    f"  - 根拠：{_text(edge['evidence_locator'])} / "
                    f"{_link('原文', edge['evidence_url'])}"
                )
                if edge.get("quote"):
                    relation_lines.append(f"  - 引用記録：{_text(edge['quote'])}")
        relation_lines.append("")
    outputs[Path("relations-view.md")] = ("\n".join(relation_lines)).encode()
    return outputs


def _expected(root: Path) -> dict[Path, bytes]:
    catalog, papers, relations = validate(root)
    expected = render(catalog, papers, relations)
    _validate_generated_links(expected)
    return expected


def _validate_generated_links(expected: dict[Path, bytes]) -> None:
    """Ensure every generated relative Markdown link names another generated view."""
    known = {path.as_posix() for path in expected}
    errors = []
    link_pattern = re.compile(r"\]\(<([^>]+)>\)")
    for source, content in expected.items():
        markdown = content.decode("utf-8")
        for target in link_pattern.findall(markdown):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            if target.startswith("/") or parsed.query or parsed.fragment:
                errors.append(f"{source}: 不正なローカルリンク: {target}")
                continue
            resolved = posixpath.normpath(posixpath.join(source.parent.as_posix(), parsed.path))
            if resolved.startswith("../") or resolved not in known:
                errors.append(f"{source}: 生成対象外へのローカルリンク: {target}")
    if errors:
        raise CatalogError("生成 Markdown のリンク検証に失敗しました:\n- " + "\n- ".join(errors))


def _unexpected_cards(root: Path, expected: dict[Path, bytes]) -> list[Path]:
    paper_dir = root / "papers"
    actual = set(paper_dir.glob("P*.md")) if paper_dir.is_dir() else set()
    wanted = {root / path for path in expected if path.parent == Path("papers")}
    return sorted(path.relative_to(root) for path in actual - wanted)


def check(root: Path) -> None:
    expected = _expected(root)
    problems = []
    for relative, content in expected.items():
        path = root / relative
        try:
            actual = path.read_bytes()
        except FileNotFoundError:
            problems.append(f"生成物がありません: {relative}")
        except OSError as exc:
            problems.append(f"生成物を読めません: {relative}: {exc}")
        else:
            if actual != content:
                problems.append(f"生成物に差分があります: {relative}")
    for relative in _unexpected_cards(root, expected):
        problems.append(f"予期しない論文カードがあります: {relative}")
    if problems:
        raise CatalogError("生成物チェックに失敗しました:\n- " + "\n- ".join(problems))


def build(root: Path) -> None:
    expected = _expected(root)
    extras = _unexpected_cards(root, expected)
    if extras:
        raise CatalogError(
            "予期しない論文カードがあるため削除せず停止しました:\n- "
            + "\n- ".join(map(str, extras))
        )
    (root / "papers").mkdir(exist_ok=True)
    for relative, content in expected.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "check"))
    parser.add_argument("--root", type=Path, default=Path.cwd(),
                        help="papers.json があるリポジトリルート（既定: カレントディレクトリ）")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "build":
            build(root)
            print("生成物を更新しました")
        else:
            check(root)
            print("データと生成物は一致しています")
    except CatalogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
