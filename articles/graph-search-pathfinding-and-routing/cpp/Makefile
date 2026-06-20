.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 graph_metrics.cpp -o graph_metrics && mkdir -p ../outputs/tables && ./graph_metrics > ../outputs/tables/cpp_graph_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f graph_metrics
