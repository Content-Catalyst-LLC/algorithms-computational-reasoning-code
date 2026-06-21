# Method Notes

This folder uses a dependency-light logistic inference workflow to illustrate machine learning as algorithmic inference.

The workflow proceeds through the following stages:

1. generate synthetic observations,
2. define features and labels,
3. split data into training and test sets,
4. fit a simple logistic model using gradient descent,
5. attach prediction scores,
6. evaluate model metrics at a default threshold,
7. sweep thresholds to expose trade-offs,
8. check calibration bins,
9. compare subgroup error patterns,
10. write a governance register.

The model is not intended to maximize performance. It is intended to make the inference pipeline visible and auditable.
