.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_api_interface.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o api-interface-haskell && ./api-interface-haskell > ../outputs/tables/haskell_api_interface.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f api-interface-haskell *.hi *.o
