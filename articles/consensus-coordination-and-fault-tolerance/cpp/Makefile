run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 consensus_metrics.cpp -o consensus_metrics && mkdir -p ../outputs/tables && ./consensus_metrics > ../outputs/tables/cpp_consensus_metrics.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f consensus_metrics
