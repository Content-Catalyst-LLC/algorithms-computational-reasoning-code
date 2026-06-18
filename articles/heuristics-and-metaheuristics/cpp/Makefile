.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 heuristic_design_audit.cpp -o heuristic_design_audit && mkdir -p ../outputs/tables && ./heuristic_design_audit > ../outputs/tables/cpp_heuristic_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f heuristic_design_audit
