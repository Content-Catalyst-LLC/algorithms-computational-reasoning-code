.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 programming_paradigm_style_audit.cpp -o programming_paradigm_style_audit && mkdir -p ../outputs/tables && ./programming_paradigm_style_audit > ../outputs/tables/cpp_programming_style_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f programming_paradigm_style_audit
