.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 space_complexity_audit.cpp -o space_complexity_audit && mkdir -p ../outputs/tables && ./space_complexity_audit > ../outputs/tables/cpp_space_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f space_complexity_audit
