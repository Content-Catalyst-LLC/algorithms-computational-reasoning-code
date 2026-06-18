.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 search_strategy_audit.cpp -o search_strategy_audit && mkdir -p ../outputs/tables && ./search_strategy_audit > ../outputs/tables/cpp_search_strategy_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f search_strategy_audit
