# Proxy Variables and Measurement Error

This companion folder supports the Sustainable Catalyst article **Proxy Variables and Measurement Error**.

It provides reproducible, teaching-oriented workflows for proxy variables, measurement error, construct validity, missingness, label error, differential error, proxy bias, causal interpretation, fairness review, validation, sensitivity analysis, and measurement governance.

## Article sequence

- Previous: `metrics-objectives-and-goodharts-law`
- Current: `proxy-variables-and-measurement-error`
- Next: `metrics-feedback-and-algorithmic-failure`

## What this folder demonstrates

- how proxy variables differ from the constructs they represent;
- how measurement error can be random, systematic, differential, missing, or label-based;
- how weak proxies create validity and fairness risk;
- how missingness and differential error can distort model training and interpretation;
- how sensitivity analysis can stress-test measurement assumptions;
- how measurement governance can document construct definitions, proxy rationales, error sources, validation plans, and use boundaries.

## Repository structure

- `python/` — reference proxy and measurement-error audit workflow and tests
- `r/` — diagnostic summaries and figures
- `sql/` — schema and governance queries for proxies, constructs, error sources, and validation
- `calculators/` — self-contained proxy-validity, measurement-risk, and misclassification calculators
- `canvas/` — Canvas-ready cards, schemas, and exports
- `docs/` — method notes, data dictionary, governance review, measurement notes, and use boundaries
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets and examples are synthetic and educational. They are not intended for operational model validation without domain review.
