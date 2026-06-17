.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 logic_computation_audit.cpp -o logic_computation_audit && mkdir -p ../outputs/tables && ./logic_computation_audit > ../outputs/tables/cpp_logic_computation_audit.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f logic_computation_audit
