.PHONY: run clean
run:
	@if command -v runhaskell >/dev/null 2>&1; then runhaskell Main.hs > ../outputs/tables/haskell_architecture_graph.csv; elif command -v ghc >/dev/null 2>&1; then ghc -O2 Main.hs -o architecture-graph-haskell && ./architecture-graph-haskell > ../outputs/tables/haskell_architecture_graph.csv; else echo "Haskell toolchain not found; skipping."; fi
clean:
	rm -f architecture-graph-haskell *.hi *.o
