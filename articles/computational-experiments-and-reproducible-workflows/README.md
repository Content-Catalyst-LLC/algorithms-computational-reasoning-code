# Computational Experiments and Reproducible Workflows

This companion folder supports the Sustainable Catalyst article **Computational Experiments and Reproducible Workflows**.

It treats computational experiments as reproducible algorithmic evidence: code, data, parameters, seeds, environments, outputs, logs, manifests, validation checks, sensitivity runs, and interpretation records preserved together.

## Article sequence

- Previous: `agent-based-algorithms-and-emergent-behavior`
- Current: `computational-experiments-and-reproducible-workflows`
- Next: `model-validation-testing-and-computational-evidence`

## Included layers

- `python/` — dependency-light reproducible experiment audit
- `r/` — base R summaries and diagnostic figures
- `calculators/` — self-contained workflow/reproducibility calculators
- `sql/` — schema for experiments, runs, artifacts, parameters, and review records
- `julia/`, `haskell/`, `rust/`, `go/`, `c`, `cpp`, `fortran`, `java`, `typescript`, `prolog`, `racket` — multilingual computational scaffolds
- `docs/` — article metadata, navigation, review checklist, and method notes
- `data/` — small synthetic scenario configuration table
- `outputs/` — generated tables, JSON summaries, figures, and logs
- `canvas/` — Canvas-ready schema/card artifacts

## Quick start

```bash
bash run_article_workflows.sh
bash run_optional_language_checks.sh
```

The workflows are synthetic, reproducible, educational, and intended for transparent computational review rather than production decision automation.
