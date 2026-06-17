.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 debugging_reasoning_audit.cpp -o debugging_reasoning_audit && mkdir -p ../outputs/tables && ./debugging_reasoning_audit > ../outputs/tables/cpp_debugging_reasoning_audit.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f debugging_reasoning_audit
