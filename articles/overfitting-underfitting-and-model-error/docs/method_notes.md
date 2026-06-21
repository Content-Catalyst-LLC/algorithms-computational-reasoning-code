# Method Notes

This folder uses synthetic polynomial-regression examples to illustrate underfitting, overfitting, validation curves, learning curves, residual diagnostics, regularization, and shifted-test fragility.

The workflow is intentionally dependency-light. It uses gradient descent rather than external numerical libraries so that the reasoning remains visible and portable across environments.

The main lesson is not that a particular polynomial degree is correct. The lesson is that training error, held-out error, residual patterns, shifted-test performance, and governance review should be interpreted together.
