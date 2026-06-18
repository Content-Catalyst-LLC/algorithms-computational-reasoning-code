.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 graph_path_metrics.cpp -o graph_path_metrics && mkdir -p ../outputs/tables && ./graph_path_metrics > ../outputs/tables/cpp_graph_path_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f graph_path_metrics
