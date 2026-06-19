.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 search_metrics.cpp -o search_metrics && mkdir -p ../outputs/tables && ./search_metrics > ../outputs/tables/cpp_search_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f search_metrics
