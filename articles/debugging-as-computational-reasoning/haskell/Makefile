.PHONY: run clean

run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_debugging_reasoning_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o debugging-haskell && ./debugging-haskell > ../outputs/tables/haskell_debugging_reasoning_cases.csv; else echo "Haskell toolchain not found; skipping."; fi

clean:
	rm -f debugging-haskell *.hi *.o
