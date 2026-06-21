# Security Failure Review Checklist

Use this checklist when reviewing a security failure as an algorithmic failure.

1. Identify the protected asset, actor, action, and resource.
2. Reconstruct the procedure the system actually followed.
3. Identify the assumptions that failed under adversarial pressure.
4. Map input, identity, data, service, tool, and governance trust boundaries.
5. Check whether authorization binds subject, resource, action, context, and time.
6. Review input validation, encoding, parsing, and context changes.
7. Review cryptographic procedures, key management, and artifact verification.
8. Review dependencies, supply-chain provenance, and configuration drift.
9. Review state, concurrency, timing, cache, transaction, and lifecycle behavior.
10. Check logs, monitoring, alerts, escalation, and incident response timing.
11. Identify incentive, metric, governance, and ownership failures.
12. Define systemic remediation, tests, monitoring rules, and review cadence.
