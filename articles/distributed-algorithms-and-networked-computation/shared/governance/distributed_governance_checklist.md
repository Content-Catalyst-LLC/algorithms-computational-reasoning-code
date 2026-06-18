# Distributed Algorithms and Networked Computation Governance Checklist

- Define system goal and global behavior.
- Inventory nodes, links, services, ownership, regions, and trust boundaries.
- Specify message schemas, security requirements, acknowledgment rules, retries, and idempotence.
- State failure model: crash, delay, partition, overload, restart, Byzantine, or adversarial behavior.
- Define consistency guarantees, read/write semantics, and user-facing freshness expectations.
- Review replication strategy, quorum rules, leader election, and failover behavior.
- Preserve correlation IDs, message IDs, trace IDs, replica versions, and source provenance.
- Monitor latency, queue depth, timeouts, retries, partial results, replica lag, and error budgets.
- Use access controls, encryption, signed messages, and least privilege across boundaries.
- Define governance gates for schema changes, replica changes, index publishing, and model/service version shifts.
