.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 online_decision_audit.cpp -o online_decision_audit && mkdir -p ../outputs/tables && ./online_decision_audit > ../outputs/tables/cpp_online_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f online_decision_audit
