.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 runtime_context_audit.cpp -o runtime_context_audit && mkdir -p ../outputs/tables && ./runtime_context_audit > ../outputs/tables/cpp_runtime_context_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f runtime_context_audit
