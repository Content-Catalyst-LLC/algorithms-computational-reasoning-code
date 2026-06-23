from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify program-as-data examples.")
parser.add_argument("--case", choices=["compiler", "interpreter", "code_generation", "malware", "supply_chain", "debugger", "version_control"], required=True)
args = parser.parse_args()

labels = {
    "compiler": "benefit_translate_program_text_to_executable_instructions",
    "interpreter": "benefit_execute_program_text_dynamically",
    "code_generation": "benefit_and_risk_generate_executable_artifacts",
    "malware": "risk_program_symbols_can_execute_harmful_behavior",
    "supply_chain": "risk_program_artifacts_move_across_institutions",
    "debugger": "benefit_inspect_program_state_and_instruction_flow",
    "version_control": "benefit_track_program_as_managed_artifact",
}
print(f"classification={labels[args.case]}")
