.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 decomposition_audit.cpp -o decomposition_audit && mkdir -p ../outputs/tables && ./decomposition_audit > ../outputs/tables/cpp_decomposition_audit.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f decomposition_audit
