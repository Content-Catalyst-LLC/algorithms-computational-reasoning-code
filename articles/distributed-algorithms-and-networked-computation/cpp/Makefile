.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 distributed_metrics.cpp -o distributed_metrics && mkdir -p ../outputs/tables && ./distributed_metrics > ../outputs/tables/cpp_distributed_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f distributed_metrics
