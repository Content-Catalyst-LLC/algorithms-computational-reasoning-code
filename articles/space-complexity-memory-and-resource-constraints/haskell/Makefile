.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_space_checks.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o space-haskell && ./space-haskell > ../outputs/tables/haskell_space_checks.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f space-haskell *.hi *.o
