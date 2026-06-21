# Evaluation, Benchmarks, and the Limits of AI Measurement

This companion folder supports the Sustainable Catalyst article **Evaluation, Benchmarks, and the Limits of AI Measurement**.

It provides reproducible, teaching-oriented workflows for AI evaluation, benchmarks, calibration, safety flags, disaggregated performance, benchmark saturation, data contamination, leaderboard review, deployment monitoring, governance documentation, and responsible computational interpretation.

## Article sequence

- Previous: `ai-agents-tool-use-and-procedural-autonomy`
- Current: `evaluation-benchmarks-and-the-limits-of-ai-measurement`
- Next: `metrics-feedback-and-algorithmic-failure`

## What this folder demonstrates

- how benchmark scores can hide calibration gaps and safety flags;
- how aggregate metrics can conceal group-level or context-level performance differences;
- how benchmark saturation can make leaderboards less diagnostic;
- how evaluation should document benchmark limits, data provenance, and deployment validity;
- how governance records can connect measurement to real approval, monitoring, and use-boundary decisions;
- how lightweight calculators can support quick metric, calibration, and benchmark-limit review.

## Repository structure

- `python/` — reference benchmark-evaluation audit workflow and tests
- `r/` — diagnostic summaries and figures
- `sql/` — schema and governance queries for benchmarks, models, metrics, and limitations
- `calculators/` — self-contained metric, calibration, and saturation calculators
- `canvas/` — Canvas-ready cards, schemas, and exports
- `docs/` — method notes, data dictionary, governance review, metric notes, and use boundaries
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets and examples are synthetic and educational. They are not intended for operational evaluation or procurement decisions.
