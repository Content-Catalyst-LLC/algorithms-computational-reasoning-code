#!/usr/bin/env bash
set -Eeuo pipefail
ARTICLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log() { printf '\n[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"; }

if command -v python3 >/dev/null 2>&1; then
  log "Running Python reference workflow"
  python3 "$ARTICLE_DIR/python/model_validation_evidence_audit.py"
else
  log "Skipping Python workflow; python3 not found"
fi

if command -v Rscript >/dev/null 2>&1; then
  log "Running R summary workflow"
  Rscript "$ARTICLE_DIR/r/model_validation_summary.R"
else
  log "Skipping R workflow; Rscript not found"
fi

log "Running calculator smoke tests"
bash "$ARTICLE_DIR/calculators/run_calculator_smoke_tests.sh"

if command -v sqlite3 >/dev/null 2>&1; then
  log "Running SQLite schema smoke test"
  sqlite3 ":memory:" < "$ARTICLE_DIR/sql/model_validation_audit_schema.sql" > "$ARTICLE_DIR/outputs/tables/sqlite_validation_schema_output.txt"
else
  log "Skipping SQLite check; sqlite3 not found"
fi

if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then
  log "Running Java metric demo"
  (cd "$ARTICLE_DIR/java" && javac ModelValidationMetrics.java && java ModelValidationMetrics > "$ARTICLE_DIR/outputs/tables/java_metrics_output.txt")
else
  log "Skipping Java check; javac/java not found"
fi

if command -v node >/dev/null 2>&1 && command -v npx >/dev/null 2>&1; then
  log "Checking TypeScript availability"
  (cd "$ARTICLE_DIR/typescript" && npx --yes ts-node model_validation_metrics.ts > "$ARTICLE_DIR/outputs/tables/typescript_metrics_output.txt") || true
else
  log "Skipping TypeScript runtime check; node/npx not found"
fi

log "Available workflow checks complete"
