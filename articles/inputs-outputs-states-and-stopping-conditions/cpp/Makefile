.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 boundary_state_audit.cpp -o boundary_state_audit && mkdir -p ../outputs/tables && ./boundary_state_audit > ../outputs/tables/cpp_boundary_state_audit.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f boundary_state_audit
