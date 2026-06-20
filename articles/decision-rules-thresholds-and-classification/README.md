# Decision Rules, Thresholds, and Classification

This companion article folder supports the Sustainable Catalyst article **Decision Rules, Thresholds, and Classification** in the **Algorithms & Computational Reasoning** series.

The folder provides lightweight, dependency-minimal workflows for exploring how computational systems turn scores, signals, evidence, and rules into classifications, thresholds, labels, actions, review paths, and governance artifacts.

## Article sequence

- Previous: `ranking-filtering-and-recommendation`
- Current: `decision-rules-thresholds-and-classification`
- Next: `linear-programming-and-convex-optimization`

## Repository contents

- `python/decision_classification/`: Python audit, threshold examples, and CLI
- `calculators/`: self-contained threshold and confusion-matrix calculators
- `r/`: base R summary workflow
- `sql/`: portable SQL schema and queries
- `julia/`, `haskell/`, `rust/`, `go/`, `c/`, `cpp/`, `fortran/`, `java/`, `typescript/`, `prolog/`, `racket/`: compact multi-language examples
- `data/`: synthetic teaching data
- `outputs/`: generated tables, JSON, and figures
- `docs/`: methodology and responsible-use notes
- `canvas/`: Canvas-ready manifest and card index
- `html/`, `css/`, `php/`: lightweight web card examples

## Quick start

```bash
make smoke
make all
```

Or run directly:

```bash
python3 python/decision_classification/audit.py
python3 python/decision_classification/cli.py --threshold 0.5
bash calculators/run_calculator_smoke_tests.sh
```

## Educational purpose

This folder is designed for transparent learning and auditability. The examples use synthetic data and should not be treated as production classification, eligibility, medical, financial, legal, hiring, or safety systems.
