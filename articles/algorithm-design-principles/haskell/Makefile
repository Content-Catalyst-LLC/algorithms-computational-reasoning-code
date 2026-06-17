.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_algorithm_design_checks.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o algorithm-design-haskell && ./algorithm-design-haskell > ../outputs/tables/haskell_algorithm_design_checks.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f algorithm-design-haskell *.hi *.o
