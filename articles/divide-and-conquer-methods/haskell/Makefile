.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_divide_conquer_checks.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o divide-conquer-haskell && ./divide-conquer-haskell > ../outputs/tables/haskell_divide_conquer_checks.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f divide-conquer-haskell *.hi *.o
