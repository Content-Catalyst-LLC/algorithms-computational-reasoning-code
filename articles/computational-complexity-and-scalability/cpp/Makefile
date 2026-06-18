.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 complexity_scalability_audit.cpp -o complexity_scalability_audit && mkdir -p ../outputs/tables && ./complexity_scalability_audit > ../outputs/tables/cpp_complexity_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f complexity_scalability_audit
