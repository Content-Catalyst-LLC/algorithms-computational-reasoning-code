from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for von Neumann architecture.")
for name in [
    "stored-program", "memory-organization", "control-structure", "program-as-data",
    "implementation-influence", "bottleneck-awareness", "collaboration-context",
    "software-relevance", "ai-infrastructure", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.stored_program +
    args.memory_organization +
    args.control_structure +
    args.program_as_data +
    args.implementation_influence +
    args.bottleneck_awareness +
    args.collaboration_context +
    args.software_relevance +
    args.ai_infrastructure +
    args.governance_caution
) / 10.0
print(f"architecture_score={score:.6f}")
