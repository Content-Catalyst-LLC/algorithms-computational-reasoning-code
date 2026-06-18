.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 performance_metrics.cpp -o performance_metrics && mkdir -p ../outputs/tables && ./performance_metrics > ../outputs/tables/cpp_performance_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f performance_metrics
