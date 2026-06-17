.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 representation_audit.cpp -o representation_audit && mkdir -p ../outputs/tables && ./representation_audit > ../outputs/tables/cpp_representation_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f representation_audit
