.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 tractability_audit.cpp -o tractability_audit && mkdir -p ../outputs/tables && ./tractability_audit > ../outputs/tables/cpp_tractability_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f tractability_audit
