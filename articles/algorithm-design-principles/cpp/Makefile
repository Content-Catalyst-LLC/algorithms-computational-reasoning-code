.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 algorithm_design_audit.cpp -o algorithm_design_audit && mkdir -p ../outputs/tables && ./algorithm_design_audit > ../outputs/tables/cpp_algorithm_design_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f algorithm_design_audit
