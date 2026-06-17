.PHONY: run clean

run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_reasoning_profiles.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o reasoning-profiles-haskell && ./reasoning-profiles-haskell > ../outputs/tables/haskell_reasoning_profiles.csv; else echo "Haskell toolchain not found; skipping."; fi

clean:
	rm -f reasoning-profiles-haskell *.hi *.o
