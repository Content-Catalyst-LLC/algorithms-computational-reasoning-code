# Consensus, Coordination, and Fault Tolerance Governance Checklist

- Define what must be agreed on: value, leader, log entry, lock, state transition, configuration, or publication gate.
- Define participants, voting rights, membership rules, terms, epochs, and fencing controls.
- State failure model: crash, omission, timing, partition, restart, Byzantine, operator, or dependency failure.
- Define quorum size, quorum intersection expectations, read/write quorum rules, and commit thresholds.
- Document leader election, failover, split-brain prevention, and stale-leader rejection.
- Make retries idempotent and preserve completion logs.
- Version logs, replicas, snapshots, model/index versions, and recovery artifacts.
- Preserve trace IDs, quorum records, term numbers, retry logs, replica versions, and governance notes.
- Expose degraded mode, partial result, read-only mode, and fail-closed conditions.
- Separate agreement from truth, source validity, authorization, and ethical acceptability.
