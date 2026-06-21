# AI Agents, Tool Use, and Procedural Autonomy

This companion folder supports the Sustainable Catalyst article **AI Agents, Tool Use, and Procedural Autonomy**.

It provides reproducible, teaching-oriented workflows for AI agents, tool use, procedural autonomy, action traces, tool permissions, approval gates, escalation logic, prompt-injection risk, monitoring, governance documentation, and responsible computational interpretation.

## Article sequence

- Previous: `automated-reasoning-symbolic-ai-and-hybrid-systems`
- Current: `ai-agents-tool-use-and-procedural-autonomy`
- Next: `evaluation-benchmarks-and-the-limits-of-ai-measurement`

## What this folder demonstrates

- how tool registries can separate read, compute, execute, draft, write, and external-write actions;
- how agent plans can be audited as state-action-observation sequences;
- how approval gates and escalation thresholds reduce autonomy risk;
- how prompt-injection and tool misuse should be recorded as procedural risks;
- how autonomy recommendations can be tied to evidence, not marketing language;
- how calculators can support quick review of permission, escalation, and autonomy levels.

## Repository structure

- `python/` — reference agent tool-use audit workflow and tests
- `r/` — diagnostic summaries and figures
- `sql/` — schema and governance queries for tools, actions, traces, and escalation
- `calculators/` — self-contained permission, escalation, and autonomy calculators
- `canvas/` — Canvas-ready cards, schemas, and exports
- `docs/` — method notes, data dictionary, governance review, security notes, and use boundaries
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All datasets and examples are synthetic and educational. They are not intended for operational deployment.
