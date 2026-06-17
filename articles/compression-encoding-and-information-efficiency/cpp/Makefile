.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 compression_encoding_audit.cpp -o compression_encoding_audit && mkdir -p ../outputs/tables && ./compression_encoding_audit > ../outputs/tables/cpp_compression_encoding_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f compression_encoding_audit
