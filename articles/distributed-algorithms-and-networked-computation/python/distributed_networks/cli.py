from pathlib import Path
import json
from distributed_networks.workflow import run_workflow, quorum_size, crash_fault_tolerance, availability_with_replication, distributed_latency, distributed_risk_score

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "quorum_5_nodes": {"majority_quorum": quorum_size(5), "crash_fault_tolerance": crash_fault_tolerance(5)},
        "availability_three_replicas": {"availability": availability_with_replication(3, .99)},
        "latency_example": {"response_ms": distributed_latency(35,80,20)},
        "distributed_risk": distributed_risk_score(.84,.80,.82,.78,.84,.78,.80)
    }
    (root/"outputs"/"json"/"distributed_networks_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Distributed algorithms and networked computation workflow complete.")
