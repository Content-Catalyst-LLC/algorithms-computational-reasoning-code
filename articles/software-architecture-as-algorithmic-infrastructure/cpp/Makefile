.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 software_architecture_audit.cpp -o software_architecture_audit && mkdir -p ../outputs/tables && ./software_architecture_audit > ../outputs/tables/cpp_software_architecture_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f software_architecture_audit
