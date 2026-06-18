.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 cloud_metrics.cpp -o cloud_metrics && mkdir -p ../outputs/tables && ./cloud_metrics > ../outputs/tables/cpp_cloud_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f cloud_metrics
