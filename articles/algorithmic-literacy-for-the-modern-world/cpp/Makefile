.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 algorithmic_literacy_audit.cpp -o algorithmic_literacy_audit && mkdir -p ../outputs/tables && ./algorithmic_literacy_audit > ../outputs/tables/cpp_algorithmic_literacy_audit.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f algorithmic_literacy_audit
