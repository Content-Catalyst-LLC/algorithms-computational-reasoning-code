from __future__ import annotations

from pathlib import Path
import csv
import json
import subprocess
import sys
import unittest

ARTICLE_ROOT = Path(__file__).resolve().parents[1]


class MeasurementAuditWorkflowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run([sys.executable, str(ARTICLE_ROOT / "python" / "features_labels_measurement_audit.py")], check=True)

    def test_summary_outputs_exist(self) -> None:
        self.assertTrue((ARTICLE_ROOT / "outputs" / "tables" / "measurement_audit_summary.csv").exists())
        self.assertTrue((ARTICLE_ROOT / "outputs" / "json" / "measurement_audit_summary.json").exists())

    def test_metrics_include_all_and_groups(self) -> None:
        path = ARTICLE_ROOT / "outputs" / "tables" / "measurement_metrics_by_group.csv"
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual({row["group"] for row in rows}, {"ALL", "A", "B"})
        for row in rows:
            self.assertGreaterEqual(float(row["label_disagreement_rate"]), 0.0)
            self.assertLessEqual(float(row["label_disagreement_rate"]), 1.0)

    def test_summary_has_governance_review_items(self) -> None:
        payload = json.loads((ARTICLE_ROOT / "outputs" / "json" / "measurement_audit_summary.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(int(payload["governance_items_requiring_review"]), 1)
        self.assertIn("measurement decisions", payload["interpretation"])


if __name__ == "__main__":
    unittest.main()
