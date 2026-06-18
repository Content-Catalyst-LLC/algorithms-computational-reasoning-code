.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 pipeline_quality_metrics.cpp -o pipeline_quality_metrics && mkdir -p ../outputs/tables && ./pipeline_quality_metrics > ../outputs/tables/cpp_pipeline_quality_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f pipeline_quality_metrics
