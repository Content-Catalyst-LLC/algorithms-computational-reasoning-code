from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify example problem families for Church-style computability teaching.")
parser.add_argument("--problem", choices=["beta_reduce_specific_term", "type_check_simply_typed_term", "entscheidungsproblem", "halting_problem", "program_equivalence", "ai_truthfulness"], required=True)
args = parser.parse_args()

labels = {
    "beta_reduce_specific_term": "computable_for_given_finite_reduction_strategy_but_may_not_terminate",
    "type_check_simply_typed_term": "decidable_in_standard_simple_type_systems",
    "entscheidungsproblem": "undecidable_in_general",
    "halting_problem": "undecidable_in_general",
    "program_equivalence": "undecidable_in_general_for_rich_languages",
    "ai_truthfulness": "evaluation_dependent_not_simple_formal_decision_problem",
}
print(f"decidability_scope={labels[args.problem]}")
