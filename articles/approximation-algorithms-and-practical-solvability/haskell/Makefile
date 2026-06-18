.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_approximation_checks.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o approximation-haskell && ./approximation-haskell > ../outputs/tables/haskell_approximation_checks.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f approximation-haskell *.hi *.o
