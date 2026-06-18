.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 parallel_speedup_metrics.cpp -o parallel_speedup_metrics && mkdir -p ../outputs/tables && ./parallel_speedup_metrics > ../outputs/tables/cpp_parallel_speedup_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f parallel_speedup_metrics
