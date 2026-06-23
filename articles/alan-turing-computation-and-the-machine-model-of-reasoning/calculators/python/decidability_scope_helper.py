from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify example problem families for teaching decidability boundaries.")
parser.add_argument("--problem", choices=["integer_addition", "sorting", "finite_state_reachability", "halting_problem", "general_program_equivalence", "loan_approval", "ai_truthfulness"], required=True)
args = parser.parse_args()

labels = {
    "integer_addition": "decidable_and_computable",
    "sorting": "decidable_and_computable",
    "finite_state_reachability": "decidable_for_finite_systems",
    "halting_problem": "undecidable_in_general",
    "general_program_equivalence": "undecidable_in_general",
    "loan_approval": "computable_but_governance_dependent",
    "ai_truthfulness": "evaluation_dependent_not_simple_decision_problem",
}
print(f"decidability_scope={labels[args.problem]}")
