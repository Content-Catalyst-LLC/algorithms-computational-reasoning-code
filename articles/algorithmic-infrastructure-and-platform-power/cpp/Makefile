.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 platform_metrics.cpp -o platform_metrics && mkdir -p ../outputs/tables && ./platform_metrics > ../outputs/tables/cpp_platform_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f platform_metrics
