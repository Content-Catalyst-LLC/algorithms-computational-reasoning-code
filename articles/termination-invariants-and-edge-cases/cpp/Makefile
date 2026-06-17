.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 boundary_reliability_audit.cpp -o boundary_reliability_audit && mkdir -p ../outputs/tables && ./boundary_reliability_audit > ../outputs/tables/cpp_boundary_reliability_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f boundary_reliability_audit
