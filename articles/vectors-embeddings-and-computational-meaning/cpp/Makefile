.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 embedding_representation_audit.cpp -o embedding_representation_audit && mkdir -p ../outputs/tables && ./embedding_representation_audit > ../outputs/tables/cpp_embedding_representation_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f embedding_representation_audit
