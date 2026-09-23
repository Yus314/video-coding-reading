"""Small structural guards for authored reading guides, not semantic proof."""
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


class ReadingIntegrityTests(unittest.TestCase):
    def test_authored_and_generated_relative_links(self):
        for path in ROOT.rglob('*.md'):
            for raw in re.findall(r'\]\((<[^>]*>|[^)\s]+)\)', path.read_text(encoding='utf-8')):
                target = raw[1:-1] if raw.startswith('<') else raw
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                dest = unquote(target.split('#')[0])
                with self.subTest(page=path.name, target=target):
                    self.assertTrue((path.parent / dest).is_file())

    def test_independent_candidates_have_decisions_and_valid_aliases(self):
        papers = {p['id']: p for p in load('papers.json')['papers']}
        candidates = load('independent-review.json')['candidates']
        self.assertEqual(len(candidates), len({c['id'] for c in candidates}))
        for c in candidates:
            self.assertTrue(c['decision'].strip())
            self.assertTrue(c['comparison_with_existing'].strip())
            alias = c.get('canonical_paper_id')
            if alias:
                self.assertIn(alias, papers)
                self.assertEqual(c['title'].casefold(), papers[alias]['title'].casefold())

    def test_paper_and_candidate_mentions_resolve(self):
        ids = {p['id'] for p in load('papers.json')['papers']}
        ids.update(c['id'] for c in load('independent-review.json')['candidates'])
        for path in ROOT.glob('*.md'):
            for identifier in re.findall(r'(?<![A-Za-z0-9])(?:IC|P)\d{2,}(?!\d)', path.read_text(encoding='utf-8')):
                self.assertIn(identifier, ids, f'{path.name}: {identifier}')

    def test_figure_and_audit_records_have_resolvable_scope(self):
        ids = {p['id'] for p in load('papers.json')['papers']}
        figures = load('figure-checks.json')['figures']
        keys = [(f['paper'], f['version'], f['locator']) for f in figures]
        self.assertEqual(len(keys), len(set(keys)))
        for f in figures:
            self.assertIn(f['paper'], ids)
            for key in ('version', 'locator', 'observed', 'reading_action'):
                self.assertTrue(f[key].strip())
            self.assertIn(urlsplit(f['url']).scheme, ('http', 'https'))
        audit = load('evidence-audit.json')
        self.assertIn(audit['paper_id'], ids)
        source_ids = {s['id'] for s in audit['sources']}
        for item in audit['resolved_uncertainties']:
            self.assertTrue(set(item['source_ids']) <= source_ids)


if __name__ == '__main__':
    unittest.main()
