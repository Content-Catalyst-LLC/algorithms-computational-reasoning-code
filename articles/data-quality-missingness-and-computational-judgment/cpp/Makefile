.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 data_quality_metrics.cpp -o data_quality_metrics && mkdir -p ../outputs/tables && ./data_quality_metrics > ../outputs/tables/cpp_data_quality_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f data_quality_metrics
