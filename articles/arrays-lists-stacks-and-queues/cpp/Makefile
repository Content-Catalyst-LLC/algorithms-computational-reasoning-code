.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 sequence_structure_audit.cpp -o sequence_structure_audit && mkdir -p ../outputs/tables && ./sequence_structure_audit > ../outputs/tables/cpp_sequence_structure_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f sequence_structure_audit
