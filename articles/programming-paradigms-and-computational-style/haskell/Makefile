.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_programming_style_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o programming-style-haskell && ./programming-style-haskell > ../outputs/tables/haskell_programming_style_cases.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f programming-style-haskell *.hi *.o
