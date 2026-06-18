.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 control_flow_audit.cpp -o control_flow_audit && mkdir -p ../outputs/tables && ./control_flow_audit > ../outputs/tables/cpp_control_flow_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f control_flow_audit
