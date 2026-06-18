.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 search_sorting_audit.cpp -o search_sorting_audit && mkdir -p ../outputs/tables && ./search_sorting_audit > ../outputs/tables/cpp_search_sorting_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f search_sorting_audit
