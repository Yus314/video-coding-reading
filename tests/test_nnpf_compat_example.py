"""Guards for the pedagogical trace, not codec conformance tests."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('example', ROOT / 'scripts/nnpf_compat_example.py')
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CompatibilityExampleTests(unittest.TestCase):
    def test_known_ue_values(self):
        self.assertEqual(module.ue(0), '1')
        self.assertEqual(module.ue(1), '010')
        self.assertEqual(module.ue(16), '000010001')
        with self.assertRaises(ValueError):
            module.ue(-1)

    def test_first_misread_and_explicit_limit(self):
        data = module.example()
        before = data['before_relocation']
        self.assertEqual(before['bits'], '01011')
        self.assertEqual(before['extension_aware']['component_last_flag'], 1)
        self.assertEqual(before['v4_first_read']['value'], 0)
        after = data['merged_design_intent']
        self.assertTrue(after['new_syntax_gate'])
        self.assertEqual(after['alternative_versions'], 2)
        self.assertFalse(after['conformance_claim'])
        self.assertIn('16..255', after['unresolved'])


if __name__ == '__main__':
    unittest.main()
