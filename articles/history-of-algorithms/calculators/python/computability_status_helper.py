from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Label example problem families for teaching computability cautions.")
parser.add_argument("--problem", choices=["sorting", "shortest_path", "halting_problem", "general_program_correctness", "loan_approval", "content_recommendation"], required=True)
args = parser.parse_args()

labels = {
    "sorting": "computable_algorithmic_problem",
    "shortest_path": "computable_algorithmic_problem",
    "halting_problem": "undecidable_general_problem",
    "general_program_correctness": "formally_limited_or_undecidable_in_general",
    "loan_approval": "computable_but_governance_dependent",
    "content_recommendation": "computable_but_feedback_and_governance_dependent",
}
print(f"computability_status={labels[args.problem]}")
