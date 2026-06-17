.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_formal_language_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o formal-language-haskell && ./formal-language-haskell > ../outputs/tables/haskell_formal_language_cases.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f formal-language-haskell *.hi *.o
