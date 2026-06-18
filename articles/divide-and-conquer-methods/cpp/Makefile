.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 divide_conquer_audit.cpp -o divide_conquer_audit && mkdir -p ../outputs/tables && ./divide_conquer_audit > ../outputs/tables/cpp_divide_conquer_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f divide_conquer_audit
