# Method Notes

This folder separates three learning paradigms:

1. **Supervised learning** uses labeled examples to learn a mapping from features to target labels.
2. **Unsupervised learning** searches for structure without target labels, here using a compact k-means-style procedure.
3. **Reinforcement learning** updates action choices using reward feedback, here through a simple epsilon-greedy bandit.

The implementations are dependency-light and deliberately transparent. They are not optimized libraries. Their purpose is to make the reasoning structure visible.
