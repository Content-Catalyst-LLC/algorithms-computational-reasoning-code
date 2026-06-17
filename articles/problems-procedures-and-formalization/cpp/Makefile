.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 formalization_audit.cpp -o formalization_audit && mkdir -p ../outputs/tables && ./formalization_audit > ../outputs/tables/cpp_formalization_audit.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f formalization_audit
