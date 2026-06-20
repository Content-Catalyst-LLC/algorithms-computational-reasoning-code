.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 optimization_metrics.cpp -o optimization_metrics && mkdir -p ../outputs/tables && ./optimization_metrics > ../outputs/tables/cpp_optimization_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f optimization_metrics
