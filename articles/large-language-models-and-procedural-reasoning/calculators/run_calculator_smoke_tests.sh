#!/usr/bin/env bash
set -euo pipefail
mkdir -p calculators/outputs
python3 calculators/python/procedural_score_calculator.py --steps-found 4 --minimum-steps 3 > calculators/outputs/procedural_score_smoke.txt
python3 calculators/python/source_support_calculator.py --expected 'source:a;source:b' --found 'source:a;source:b' --requires-sources > calculators/outputs/source_support_smoke.txt
python3 calculators/python/risk_escalation_calculator.py --procedural-score 1 --source-score 0 --risk-score 1 --stakes high > calculators/outputs/risk_escalation_smoke.txt
python3 calculators/python/context_budget_calculator.py --context-window 8192 --system-words 500 --prompt-words 700 --retrieved-words 1500 --reserved-output-tokens 1200 > calculators/outputs/context_budget_smoke.txt
if command -v Rscript >/dev/null 2>&1; then Rscript calculators/r/source_support_calculator.R 'source:a;source:b' 'source:a;source:b' > calculators/outputs/r_source_support_smoke.txt; else echo 'Rscript not found; skipping R calculator.' > calculators/outputs/r_source_support_smoke.txt; fi
echo "calculator smoke tests complete"
