.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 parallelism_scale_audit.cpp -o parallelism_scale_audit && mkdir -p ../outputs/tables && ./parallelism_scale_audit > ../outputs/tables/cpp_parallelism_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f parallelism_scale_audit
