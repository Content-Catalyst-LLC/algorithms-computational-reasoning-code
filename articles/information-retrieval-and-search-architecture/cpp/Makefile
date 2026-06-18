.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 retrieval_metrics.cpp -o retrieval_metrics && mkdir -p ../outputs/tables && ./retrieval_metrics > ../outputs/tables/cpp_retrieval_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f retrieval_metrics
