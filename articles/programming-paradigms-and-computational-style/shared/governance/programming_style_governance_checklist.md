# Programming Style Governance Checklist

- Define the problem shape: procedural, transformational, relational, interactive, concurrent, distributed, analytical, or hybrid.
- Choose the primary computational style that makes the core reasoning clearest.
- Document where state lives and who can change it.
- Separate pure computation from side effects where practical.
- Define abstractions: functions, classes, modules, services, rules, queries, actors, or pipelines.
- Use tests that match the chosen style.
- Make errors explicit, recoverable, logged, and reviewable.
- Preserve traceability for inputs, state changes, outputs, and decisions.
- Document style conventions and architecture boundaries.
- Review style drift, hidden coupling, fragile scripts, and architectural erosion over time.
