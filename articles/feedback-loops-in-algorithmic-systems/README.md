# Feedback Loops in Algorithmic Systems

This companion folder supports the Sustainable Catalyst article **Feedback Loops in Algorithmic Systems**.

It provides reproducible, teaching-oriented workflows for algorithmic feedback loops, exposure bias, popularity bias, self-fulfilling prediction, performative prediction, recursive data, drift monitoring, intervention tracking, correction pathways, and feedback governance.

## Article sequence

- Previous: `proxy-variables-and-measurement-error`
- Current: `feedback-loops-in-algorithmic-systems`
- Next: `metrics-feedback-and-algorithmic-failure`

## What this folder demonstrates

- how algorithmic outputs can reshape future inputs;
- how ranking and recommendation systems create exposure feedback;
- how predictions can become interventions that change recorded outcomes;
- how recursive data and generated outputs can enter future training pipelines;
- how drift, amplification, and intervention influence can be audited;
- how governance records can document feedback maps, exposure logs, intervention tracking, drift monitoring, and correction pathways.

## Repository structure

- `python/` — reference algorithmic feedback-loop audit workflow and tests
- `r/` — diagnostic summaries and figures
- `sql/` — schema and governance queries for feedback paths, drift, exposure, and intervention records
- `calculators/` — self-contained amplification, drift, and recursive-data calculators
- `canvas/` — Canvas-ready cards, schemas, and exports
- `docs/` — method notes, data dictionary, governance review, feedback notes, and use boundaries
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets and examples are synthetic and educational. They are not intended for operational system monitoring without domain validation.
