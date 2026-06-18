# Streaming Algorithms Governance Checklist

- Define the stream source, event schema, expected arrival rate, and processing rate.
- State the memory budget and retained streaming state.
- Define windows, event time, processing time, watermarks, and late-data policy.
- Document whether outputs are exact, approximate, sampled, delayed, revised, or provisional.
- State error bounds, false-positive rates, false-negative risks, and uncertainty language.
- Test throughput, backpressure, dropped data, duplicate events, and replay behavior.
- Review sampling design for rare-event visibility and fairness.
- Govern alerts, escalation, fatigue, response capacity, and accountability.
- Define retention for raw events, summaries, sketches, logs, and audit traces.
- Review privacy implications of continuous behavioral monitoring.
