.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_execution_model_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o execution-models-haskell && ./execution-models-haskell > ../outputs/tables/haskell_execution_model_cases.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f execution-models-haskell *.hi *.o
