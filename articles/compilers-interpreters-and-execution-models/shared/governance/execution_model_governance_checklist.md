# Execution Model Governance Checklist

- Identify source language, target representation, and runtime.
- Map translation stages from source code to executable behavior.
- Document semantic checks: syntax, scopes, types, permissions, and constraints.
- Record compiler, interpreter, runtime, OS, architecture, and dependency versions.
- Preserve build scripts, lockfiles, generated artifacts, checksums, and release provenance.
- Review optimization settings and debug/release differences.
- Maintain useful diagnostics, stack traces, source maps, logs, and profiler outputs.
- Define trust boundaries, sandboxing, permissions, and resource limits.
- Test portability across target platforms and execution contexts.
- Treat execution as a governed process, not an invisible final step.
