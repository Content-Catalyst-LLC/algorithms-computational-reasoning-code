.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_automated_reasoning_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o automated-reasoning-haskell && ./automated-reasoning-haskell > ../outputs/tables/haskell_automated_reasoning_cases.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f automated-reasoning-haskell *.hi *.o
