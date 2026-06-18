.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 p_np_hardness_audit.cpp -o p_np_hardness_audit && mkdir -p ../outputs/tables && ./p_np_hardness_audit > ../outputs/tables/cpp_p_np_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f p_np_hardness_audit
