# Distribution Shift and Model Decay

This companion folder supports the Sustainable Catalyst article **Distribution Shift and Model Decay**.

It provides reproducible, teaching-oriented workflows for distribution shift, model decay, covariate shift, label shift, concept drift, temporal drift, calibration drift, monitoring triggers, retraining review, rollback planning, and accountable model lifecycle governance.

## Article sequence

- Previous: `feedback-loops-in-algorithmic-systems`
- Current: `distribution-shift-and-model-decay`
- Next: `metrics-feedback-and-algorithmic-failure`

## What this folder demonstrates

- how deployment data can differ from training, validation, and test data;
- how model performance, calibration, fairness, safety, and usefulness can decay over time;
- how drift signals can appear in inputs, labels, outputs, subgroups, and override behavior;
- how retraining can help or harm depending on data provenance and feedback contamination;
- how rollback, pause, review, and sunset plans support responsible deployment;
- how monitoring records can connect model performance to governance decisions.

## Repository structure

- `python/` — reference drift-and-decay audit workflow and tests
- `r/` — diagnostic summaries and figures
- `sql/` — schema and governance queries for drift, decay, monitoring, and rollback review
- `calculators/` — self-contained drift, decay, calibration, and threshold calculators
- `canvas/` — Canvas-ready cards, schemas, and exports
- `docs/` — method notes, data dictionary, governance review, monitoring notes, and use boundaries
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets and examples are synthetic and educational. They are not intended for operational model monitoring without domain validation.
