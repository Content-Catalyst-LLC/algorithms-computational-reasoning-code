.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 verification_audit.cpp -o verification_audit && mkdir -p ../outputs/tables && ./verification_audit > ../outputs/tables/cpp_verification_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f verification_audit
