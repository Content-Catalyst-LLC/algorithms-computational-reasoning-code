.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 execution_model_audit.cpp -o execution_model_audit && mkdir -p ../outputs/tables && ./execution_model_audit > ../outputs/tables/cpp_execution_model_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f execution_model_audit
