# Metrics, Objectives, and Goodhart's Law

This companion folder supports the Sustainable Catalyst article **Metrics, Objectives, and Goodhart's Law**.

It provides reproducible, teaching-oriented workflows for metric-objective alignment, Goodhart risk, Campbell's Law, proxy-goal drift, reward hacking, benchmark gaming, incentive distortion, guardrail metrics, monitoring, and accountable measurement governance.

## Article sequence

- Previous: `evaluation-benchmarks-and-the-limits-of-ai-measurement`
- Current: `metrics-objectives-and-goodharts-law`
- Next: `metrics-feedback-and-algorithmic-failure`

## What this folder demonstrates

- how metrics differ from objectives;
- how proxies degrade under optimization pressure;
- how Goodhart risk can be summarized through proxy alignment, gaming risk, and guardrail coverage;
- how target pressure can distort institutions, platforms, and AI systems;
- how multi-metric governance can track primary metrics, guardrails, equity metrics, quality metrics, and drift signals;
- how lightweight calculators can support quick proxy-gap, guardrail, and Goodhart-risk review.

## Repository structure

- `python/` — reference Goodhart-risk audit workflow and tests
- `r/` — diagnostic summaries and figures
- `sql/` — schema and governance queries for metrics, objectives, proxies, and risk checks
- `calculators/` — self-contained proxy-gap, Goodhart-risk, and guardrail calculators
- `canvas/` — Canvas-ready cards, schemas, and exports
- `docs/` — method notes, data dictionary, governance review, metric notes, and use boundaries
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets and examples are synthetic and educational. They are not intended for operational metric governance without domain validation.
