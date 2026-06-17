.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_state_machine.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o state-machine-haskell && ./state-machine-haskell > ../outputs/tables/haskell_state_machine.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f state-machine-haskell *.hi *.o
