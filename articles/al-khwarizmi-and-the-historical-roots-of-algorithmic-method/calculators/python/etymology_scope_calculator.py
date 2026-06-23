from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify the scope of algorithm-related historical terms.")
parser.add_argument("--term", choices=["khwarizmi", "algorism", "algorithm", "formal_algorithm", "program", "algorithmic_system"], required=True)
args = parser.parse_args()

definitions = {
    "khwarizmi": "historical_scholar_connected_to_word_history_and_method_history",
    "algorism": "written_arithmetic_with_hindu_arabic_numerals",
    "algorithm": "general_method_of_computation_broadened_over_time",
    "formal_algorithm": "modern_finite_effective_procedure",
    "program": "machine_executable_implementation",
    "algorithmic_system": "procedure_data_software_institution_and_governance",
}
print(f"scope={definitions[args.term]}")
