.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 algorithmic_reasoning.cpp -o algorithmic_reasoning && mkdir -p ../outputs/tables && ./algorithmic_reasoning > ../outputs/tables/cpp_algorithmic_reasoning.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f algorithmic_reasoning
