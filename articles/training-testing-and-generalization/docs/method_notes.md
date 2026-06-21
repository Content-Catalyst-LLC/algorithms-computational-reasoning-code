# Method Notes

This folder demonstrates why training performance is not enough. The Python workflow separates fitting data from held-out test data, evaluates a shifted test set, reports cross-validation stability, computes calibration summaries, and records risks that should be reviewed before making deployment claims.

The model is intentionally compact and dependency-free. It is not meant to compete with production machine-learning libraries. Its purpose is to make the logic of training, testing, and generalization visible.
