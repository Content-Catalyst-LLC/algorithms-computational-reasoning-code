.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 metadata_provenance_audit.cpp -o metadata_provenance_audit && mkdir -p ../outputs/tables && ./metadata_provenance_audit > ../outputs/tables/cpp_metadata_provenance_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f metadata_provenance_audit
