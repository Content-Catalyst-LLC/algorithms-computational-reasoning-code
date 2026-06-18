.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 greedy_algorithm_audit.cpp -o greedy_algorithm_audit && mkdir -p ../outputs/tables && ./greedy_algorithm_audit > ../outputs/tables/cpp_greedy_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f greedy_algorithm_audit
