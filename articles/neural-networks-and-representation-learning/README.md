# Neural Networks and Representation Learning

This companion folder supports the Sustainable Catalyst article **Neural Networks and Representation Learning**.

It provides reproducible, teaching-oriented workflows for learned representations, synthetic neural-style training, train/test behavior, representation gaps, embedding diagnostics, hidden-layer review, loss curves, robustness concerns, interpretability artifacts, governance registers, and responsible deployment boundaries.

## Article sequence

- Previous: `overfitting-underfitting-and-model-error`
- Current: `neural-networks-and-representation-learning`
- Next: `large-language-models-and-procedural-reasoning`

## What this folder demonstrates

This folder treats neural networks as computational reasoning systems. It does not attempt to reproduce large-scale deep learning frameworks. Instead, it offers compact, dependency-light examples that make the core reasoning visible:

1. how inputs are transformed into learned representations;
2. how training loss and test loss differ;
3. how a representation can separate labels while still requiring validity review;
4. how embeddings can support similarity while hiding assumptions;
5. how governance artifacts should bound model use.

## Contents

- `python/` — reference representation-learning audit workflow and tests
- `r/` — diagnostic summaries and plots
- `sql/` — schema and review queries for representation audits
- `calculators/` — self-contained calculators for representation scores, cosine similarity, generalization gaps, and gradient updates
- `docs/` — method notes, data dictionary, governance checklist, and use-boundary notes
- `canvas/` — Canvas-ready cards, schemas, and exports
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets are synthetic and educational. They are not intended for operational decisions.

## Quick start

```bash
make run
make test
make calculator-smoke
```

Optional R diagnostics run automatically when `Rscript` is available.
