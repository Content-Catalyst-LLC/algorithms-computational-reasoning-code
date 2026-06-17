.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 computability_boundary_audit.cpp -o computability_boundary_audit && mkdir -p ../outputs/tables && ./computability_boundary_audit > ../outputs/tables/cpp_computability_boundary_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f computability_boundary_audit
