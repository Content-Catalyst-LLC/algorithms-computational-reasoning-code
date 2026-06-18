.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 big_o_growth_audit.cpp -o big_o_growth_audit && mkdir -p ../outputs/tables && ./big_o_growth_audit > ../outputs/tables/cpp_big_o_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f big_o_growth_audit
