.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 approximation_algorithm_audit.cpp -o approximation_algorithm_audit && mkdir -p ../outputs/tables && ./approximation_algorithm_audit > ../outputs/tables/cpp_approximation_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f approximation_algorithm_audit
