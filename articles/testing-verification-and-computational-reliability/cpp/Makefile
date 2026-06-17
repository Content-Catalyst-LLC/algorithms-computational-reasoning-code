.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 reliability_audit.cpp -o reliability_audit && mkdir -p ../outputs/tables && ./reliability_audit > ../outputs/tables/cpp_reliability_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f reliability_audit
