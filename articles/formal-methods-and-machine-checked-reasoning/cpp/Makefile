.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 formal_methods_audit.cpp -o formal_methods_audit && mkdir -p ../outputs/tables && ./formal_methods_audit > ../outputs/tables/cpp_formal_methods_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f formal_methods_audit
