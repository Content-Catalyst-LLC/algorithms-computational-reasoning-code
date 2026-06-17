.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 lambda_reasoning_audit.cpp -o lambda_reasoning_audit && mkdir -p ../outputs/tables && ./lambda_reasoning_audit > ../outputs/tables/cpp_lambda_reasoning_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f lambda_reasoning_audit
