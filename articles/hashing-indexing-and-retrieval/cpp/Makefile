.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 hashing_retrieval_audit.cpp -o hashing_retrieval_audit && mkdir -p ../outputs/tables && ./hashing_retrieval_audit > ../outputs/tables/cpp_hashing_retrieval_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f hashing_retrieval_audit
