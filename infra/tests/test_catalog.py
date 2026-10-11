"""Focused extractor checks; no verifier or broad Aegis campaign is invoked."""
from argparse import Namespace
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.catalog import candidates_for, cpp_case, inventory, python_case, qualify


class TestCatalogExtraction(unittest.TestCase):
    def test_fixture_and_transitive_setup_are_extracted_from_source(self):
        sources = {
            "case.py": "from destiny.test import helpers\nclass Ball(helpers.Base):\n def test_slot(self):\n  ball = helpers.make(self.park)\n  self.assertEqual(ball.slot, helpers.SLOT)\n",
            "python/destiny/test/helpers.py": "import unittest\nSLOT = 2\nDEFAULT = 7\nclass Base(unittest.TestCase):\n def setUp(self):\n  self.park = DEFAULT\n def tearDown(self):\n  del self.park\ndef make(park):\n return park\n",
        }
        value = python_case("case.py", "test_slot", None, sources.__getitem__)
        self.assertEqual(value["fixture"], "Ball")
        text = "\n".join(s["text"] for s in value["snippets"])
        for expected in ("def setUp", "def tearDown", "DEFAULT = 7", "SLOT = 2", "def make", "self.assertEqual"):
            self.assertIn(expected, text)
        self.assertEqual([r["class"] for r in value["fixture_chain"]], ["Ball", "Base"])
        self.assertEqual(value["assertion_lines"], [5])

    def test_duplicate_names_select_each_original_fixture_automatically(self):
        text = "class First:\n def test_same(self):\n  assert 1 == 1\nclass Second:\n def test_same(self):\n  assert 2 == 2\n"
        read = lambda _: text
        first = python_case("case.py", "test_same", None, read)
        second = python_case("case.py", "test_same", None, read, completed={"First"})
        self.assertEqual((first["fixture"], second["fixture"]), ("First", "Second"))
        self.assertEqual(first["matching_original_definitions"], 2)
        done = python_case("case.py", "test_same", None, read, completed={"First", "Second"})
        self.assertEqual(done["status"], "WORK_ALREADY_RECORDED")

    def test_catalog_preserves_repeated_entries(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "verification/spec/src/catalog.rs"
            path.parent.mkdir(parents=True)
            path.write_text('file!("case.py" => ["test_same", "test_same"])')
            self.assertEqual(inventory(root)["case.py::test_same"], 2)
            rows = qualify(inventory(root), lambda _: "class First:\n def test_same(self): pass\nclass Second:\n def test_same(self): pass\n")
            self.assertEqual([r["id"] for r in rows], ["case.py::First::test_same", "case.py::Second::test_same"])
            marked = {"case.py::test_same": [{"path": "old.rs", "line": 1}]}
            for row in rows:
                actual, ambiguous = candidates_for(row, marked)
                self.assertEqual(actual, [])
                self.assertEqual(len(ambiguous), 1)
            with self.assertRaisesRegex(ValueError, "multiplicity"):
                qualify(inventory(root), lambda _: "class First:\n def test_same(self): pass\n")

    def test_cpp_preserves_setup_assertions_and_ignores_comment_braces(self):
        text = '#include "fixture.h"\nconst int INITIAL = 2;\nTEST( Shape, Zero ) {\n // } is a comment\n auto value = INITIAL;\n ASSERT_EQ(value, 2);\n}\nTEST( Other, Zero ) { ASSERT_EQ(3, 3); }\n'
        value = cpp_case("case.cpp", "Zero", None, lambda _: text)
        self.assertEqual(value["fixture"], "Shape")
        self.assertIn("ASSERT_EQ(value, 2)", value["snippets"][0]["text"])
        self.assertIn("INITIAL = 2", value["snippets"][1]["text"])
        second = cpp_case("case.cpp", "Zero", None, lambda _: text, completed={"Shape"})
        self.assertEqual(second["fixture"], "Other")

    def test_missing_original_case_never_invents_a_fixture(self):
        value = python_case("case.py", "missing", None, lambda _: "class Base: pass\n")
        self.assertEqual(value["status"], "SOURCE_MAPPING_REQUIRED")
        self.assertEqual(value["fixtures"], [])

    def test_cpp_selected_fixture_can_be_declared_after_other_tests(self):
        text = 'TEST(Earlier, Same) { ASSERT_EQ(1, 1); }\nclass Selected : public ::testing::Test {\n void SetUp() { value = 10; }\n int value;\n};\nTEST_F(Selected, Same) { ASSERT_EQ(value, 10); }\n'
        value = cpp_case("case.cpp", "Same", "Selected", lambda _: text)
        self.assertEqual(value["fixture"], "Selected")
        self.assertIn("void SetUp() { value = 10; }", "\n".join(s["text"] for s in value["snippets"]))


if __name__ == "__main__":
    unittest.main()
