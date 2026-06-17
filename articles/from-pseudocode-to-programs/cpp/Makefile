.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 pseudocode_translation_audit.cpp -o pseudocode_translation_audit && mkdir -p ../outputs/tables && ./pseudocode_translation_audit > ../outputs/tables/cpp_pseudocode_translation_audit.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f pseudocode_translation_audit
