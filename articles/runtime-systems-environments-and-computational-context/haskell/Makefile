.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_runtime_context.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o runtime-context-haskell && ./runtime-context-haskell > ../outputs/tables/haskell_runtime_context.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f runtime-context-haskell *.hi *.o
