.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_compression_encoding_cases.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o compression-encoding-haskell && ./compression-encoding-haskell > ../outputs/tables/haskell_compression_encoding_cases.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f compression-encoding-haskell *.hi *.o
