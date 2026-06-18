.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 relational_query_audit.cpp -o relational_query_audit && mkdir -p ../outputs/tables && ./relational_query_audit > ../outputs/tables/cpp_relational_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f relational_query_audit
