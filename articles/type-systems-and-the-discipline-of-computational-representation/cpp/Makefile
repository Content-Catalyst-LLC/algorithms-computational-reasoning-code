.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 type_representation_audit.cpp -o type_representation_audit && mkdir -p ../outputs/tables && ./type_representation_audit > ../outputs/tables/cpp_type_representation_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f type_representation_audit
