.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 efficiency_understanding_audit.cpp -o efficiency_understanding_audit && mkdir -p ../outputs/tables && ./efficiency_understanding_audit > ../outputs/tables/cpp_efficiency_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f efficiency_understanding_audit
