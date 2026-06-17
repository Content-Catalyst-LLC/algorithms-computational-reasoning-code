.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_hashing_retrieval_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o hashing-retrieval-haskell && ./hashing-retrieval-haskell > ../outputs/tables/haskell_hashing_retrieval_cases.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f hashing-retrieval-haskell *.hi *.o
