import sys
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from evaluate import (load_cases, validate_cases, select_cases, create_rows,
                      score_row, write_csv, read_csv, report, aggregate)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.cases = load_cases()

    def test_dataset_valid(self):
        counts = validate_cases(self.cases)
        self.assertEqual(len(self.cases), 40)
        self.assertEqual(counts["clean"], 8)
        for category in ("authority_spoofing", "conversation_spoofing", "grading_pressure", "format_hijack"):
            self.assertEqual(counts[category], 8)

    def test_stratified_pilot_and_two_conditions(self):
        subset = select_cases(self.cases, 10)
        self.assertEqual(len(subset), 10)
        self.assertEqual(len(set(x["category"] for x in subset)), 5)
        rows = list(create_rows(subset))
        self.assertEqual(len(rows), 20)
        self.assertEqual(len({(r["case_id"], r["condition"]) for r in rows}), 20)

    def test_scoring_is_not_a_claim_of_proven_compromise(self):
        row = list(create_rows(select_cases(self.cases, 10)))[2]
        self.assertIsNone(score_row(row))
        row["response"] = row["attack_marker"] or "arbitrary"
        score = score_row(row)
        self.assertEqual(score["marker_emitted"], bool(row["attack_marker"]))
        self.assertIn("task_correct", score)

    def test_roundtrip_and_report(self):
        rows = list(create_rows(select_cases(self.cases, 10)))
        rows[0]["response"] = rows[0]["expected_answer"]
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "responses.csv"
            write_csv(output, rows)
            restored = read_csv(output)
            self.assertEqual(len(restored), 20)
            self.assertEqual(sum(x["n"] for x in aggregate(restored).values()), 1)
            result = report(restored, "Test fixture")
            self.assertIn("1 (out of 20", result)
            self.assertIn("Test fixture", result)


if __name__ == "__main__":
    unittest.main()
