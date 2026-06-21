# Large Language Models and Procedural Reasoning

This companion folder supports the Sustainable Catalyst article **Large Language Models and Procedural Reasoning**.

It provides reproducible, teaching-oriented workflows for auditing LLM-style procedural outputs, prompt constraints, source grounding, hallucination risk, tool-use oversight, escalation decisions, evaluation artifacts, governance records, and responsible deployment boundaries.

## Article sequence

- Previous: `neural-networks-and-representation-learning`
- Current: `large-language-models-and-procedural-reasoning`
- Next: `automated-reasoning-symbolic-ai-and-hybrid-systems`

## What this folder demonstrates

This folder treats large language models as computational reasoning systems embedded in wider procedural workflows. It does not call a commercial or external LLM. Instead, it creates synthetic LLM-style outputs and audits them using transparent, dependency-light checks:

1. procedural structure and step sufficiency;
2. source-grounding and citation coverage;
3. risky certainty language;
4. stakes-sensitive escalation;
5. tool-permission and human-review requirements;
6. governance documentation for LLM-assisted workflows.

## Contents

- `python/` — reference LLM procedural-reasoning audit workflow and tests
- `r/` — diagnostic summaries and plots when R is available
- `sql/` — schema and review queries for LLM audit records
- `calculators/` — self-contained calculators for step scores, source support, risk escalation, and token budgeting
- `docs/` — method notes, data dictionary, governance checklist, prompt review notes, and use-boundary documentation
- `canvas/` — Canvas-ready cards, schemas, and exports
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets and outputs are synthetic and educational. They are not intended for operational, legal, medical, financial, or other high-stakes decisions.

## Quick start

```bash
make run
make test
make calculator-smoke
```

Optional R diagnostics run automatically when `Rscript` is available.
