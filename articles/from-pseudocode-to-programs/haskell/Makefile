.PHONY: run clean

run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_pseudocode_translation_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o translation-haskell && ./translation-haskell > ../outputs/tables/haskell_pseudocode_translation_cases.csv; else echo "Haskell toolchain not found; skipping."; fi

clean:
	rm -f translation-haskell *.hi *.o
