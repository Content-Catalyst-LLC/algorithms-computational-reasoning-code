.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 automated_reasoning_audit.cpp -o automated_reasoning_audit && mkdir -p ../outputs/tables && ./automated_reasoning_audit > ../outputs/tables/cpp_automated_reasoning_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f automated_reasoning_audit
