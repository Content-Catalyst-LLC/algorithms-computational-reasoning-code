.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 edge_metrics.cpp -o edge_metrics && mkdir -p ../outputs/tables && ./edge_metrics > ../outputs/tables/cpp_edge_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f edge_metrics
