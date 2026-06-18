.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 evolutionary_search_audit.cpp -o evolutionary_search_audit && mkdir -p ../outputs/tables && ./evolutionary_search_audit > ../outputs/tables/cpp_evolutionary_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f evolutionary_search_audit
