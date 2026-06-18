from pathlib import Path
import json
from consensus_fault_tolerance.workflow import run_workflow, majority_quorum, crash_fault_tolerance, byzantine_replica_requirement, majority_availability, consensus_risk_score
if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "quorum_5_nodes":{"majority_quorum":majority_quorum(5),"crash_fault_tolerance":crash_fault_tolerance(5)},
        "byzantine_2_faults":{"minimum_replicas_3f_plus_1":byzantine_replica_requirement(2)},
        "majority_availability_5_nodes":{"availability":majority_availability(5,.99)},
        "consensus_risk":consensus_risk_score(.88,.90,.86,.84,.82,.82,.84)
    }
    (root/"outputs"/"json"/"consensus_fault_tolerance_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Consensus, coordination, and fault tolerance workflow complete.")
