.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 halting_boundary_audit.cpp -o halting_boundary_audit && mkdir -p ../outputs/tables && ./halting_boundary_audit > ../outputs/tables/cpp_halting_boundary_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f halting_boundary_audit
