.PHONY: run clean

run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_algorithmic_reasoning.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o algorithmic-reasoning-haskell && ./algorithmic-reasoning-haskell > ../outputs/tables/haskell_algorithmic_reasoning.csv; else echo "Haskell toolchain not found; skipping."; fi

clean:
	rm -f algorithmic-reasoning-haskell *.hi *.o
