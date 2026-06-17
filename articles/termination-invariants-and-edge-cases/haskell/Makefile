.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_boundary_reliability_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o boundary-reliability-haskell && ./boundary-reliability-haskell > ../outputs/tables/haskell_boundary_reliability_cases.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f boundary-reliability-haskell *.hi *.o
