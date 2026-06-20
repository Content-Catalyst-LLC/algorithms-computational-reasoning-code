.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 constraint_metrics.cpp -o constraint_metrics && mkdir -p ../outputs/tables && ./constraint_metrics > ../outputs/tables/cpp_constraint_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f constraint_metrics
