#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "==> Running required Python workflow"
python3 python/simulation_as_computational_reasoning_audit.py
python3 calculators/python/simulation_calculator.py

if command -v Rscript >/dev/null 2>&1; then
  echo "==> Running R workflow"
  Rscript r/simulation_as_computational_reasoning_summary.R
  Rscript calculators/r/simulation_calculator.R
else
  echo "==> Rscript not found; skipping R checks"
fi

if command -v julia >/dev/null 2>&1; then julia julia/simulation_summary.jl; else echo "==> Julia not found; skipping"; fi
if command -v runghc >/dev/null 2>&1; then runghc haskell/SimulationSummary.hs; else echo "==> Haskell runghc not found; skipping"; fi
if command -v cargo >/dev/null 2>&1; then (cd rust && cargo run --quiet); else echo "==> Cargo not found; skipping Rust"; fi
if command -v go >/dev/null 2>&1; then (cd go && go run main.go); else echo "==> Go not found; skipping"; fi
if command -v gcc >/dev/null 2>&1; then gcc c/simulation.c -o /tmp/simulation_c && /tmp/simulation_c >/dev/null; else echo "==> gcc not found; skipping C"; fi
if command -v g++ >/dev/null 2>&1; then g++ cpp/simulation.cpp -o /tmp/simulation_cpp && /tmp/simulation_cpp >/dev/null; else echo "==> g++ not found; skipping C++"; fi
if command -v gfortran >/dev/null 2>&1; then gfortran fortran/simulation.f90 -o /tmp/simulation_f90 && /tmp/simulation_f90 >/dev/null; else echo "==> gfortran not found; skipping Fortran"; fi
if command -v javac >/dev/null 2>&1 && command -v java >/dev/null 2>&1; then (cd java && javac SimulationSummary.java && java SimulationSummary); else echo "==> Java runtime/compiler not found; skipping Java"; fi
if command -v ts-node >/dev/null 2>&1; then ts-node typescript/simulation.ts; elif command -v npx >/dev/null 2>&1; then npx ts-node typescript/simulation.ts || true; else echo "==> TypeScript runtime not found; skipping"; fi
if command -v swipl >/dev/null 2>&1; then swipl -q -f prolog/simulation.pl; else echo "==> SWI-Prolog not found; skipping"; fi
if command -v racket >/dev/null 2>&1; then racket racket/simulation.rkt; else echo "==> Racket not found; skipping"; fi
