.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 streaming_audit.cpp -o streaming_audit && mkdir -p ../outputs/tables && ./streaming_audit > ../outputs/tables/cpp_streaming_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f streaming_audit
