.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 randomized_algorithm_audit.cpp -o randomized_algorithm_audit && mkdir -p ../outputs/tables && ./randomized_algorithm_audit > ../outputs/tables/cpp_randomized_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f randomized_algorithm_audit
