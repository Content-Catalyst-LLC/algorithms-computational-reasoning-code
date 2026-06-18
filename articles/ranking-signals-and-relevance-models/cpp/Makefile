.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 ranking_metrics.cpp -o ranking_metrics && mkdir -p ../outputs/tables && ./ranking_metrics > ../outputs/tables/cpp_ranking_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f ranking_metrics
