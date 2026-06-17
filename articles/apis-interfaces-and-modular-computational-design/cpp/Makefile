.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 api_interface_audit.cpp -o api_interface_audit && mkdir -p ../outputs/tables && ./api_interface_audit > ../outputs/tables/cpp_api_interface_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f api_interface_audit
