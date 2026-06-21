#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/symbolic_rule_calculator.py" \
  --facts "has_documentation,logs_decisions" \
  --premises "has_documentation,logs_decisions" \
  --conclusion "traceable_system" > "$OUT/symbolic_rule_calculator_smoke.txt"

python3 "$ROOT/calculators/python/constraint_satisfaction_calculator.py" \
  --known "traceable_system,reviewable_system,hybrid_system" \
  --required "traceable_system,reviewable_system,hybrid_system,requires_escalation_review" > "$OUT/constraint_satisfaction_calculator_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/rule_trace_score.R" 5 5 > "$OUT/rule_trace_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/rule_trace_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
