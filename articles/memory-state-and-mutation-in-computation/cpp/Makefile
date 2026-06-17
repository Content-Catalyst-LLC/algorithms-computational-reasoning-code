.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 state_mutation_audit.cpp -o state_mutation_audit && mkdir -p ../outputs/tables && ./state_mutation_audit > ../outputs/tables/cpp_state_mutation_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f state_mutation_audit
