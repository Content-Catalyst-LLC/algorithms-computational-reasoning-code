from __future__ import annotations

from pathlib import Path
import importlib.util
import sys
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "neural_networks_representation_learning_audit.py"
spec = importlib.util.spec_from_file_location("representation_audit", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)


class RepresentationAuditTests(unittest.TestCase):
    def test_sigmoid_bounds(self):
        self.assertGreater(module.sigmoid(0), 0)
        self.assertLess(module.sigmoid(0), 1)
        self.assertAlmostEqual(module.sigmoid(0), 0.5)

    def test_data_generation_count(self):
        config = module.RepresentationConfig(n=25, epochs=2)
        rows = module.generate_data(config)
        self.assertEqual(len(rows), 25)
        self.assertIn("interaction_x1_x3", rows[0])

    def test_train_and_evaluate(self):
        config = module.RepresentationConfig(n=60, epochs=5)
        rows = module.generate_data(config)
        train_rows, test_rows = module.train_test_split(rows, config)
        weights, history = module.train_model(train_rows, config)
        summary, predictions = module.evaluate(test_rows, weights, "test", config.threshold)
        self.assertEqual(len(weights), 5)
        self.assertGreaterEqual(summary["accuracy"], 0)
        self.assertEqual(len(predictions), len(test_rows))
        self.assertTrue(history)

    def test_embedding_similarity_rows(self):
        rows = module.embedding_similarity_rows()
        self.assertGreaterEqual(len(rows), 3)
        self.assertIn("cosine_similarity", rows[0])


if __name__ == "__main__":
    unittest.main()
