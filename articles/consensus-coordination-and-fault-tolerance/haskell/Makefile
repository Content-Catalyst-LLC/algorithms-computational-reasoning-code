run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_consensus_checks.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f consensus-haskell *.hi *.o
