.PHONY: run clean

run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 reasoning_profiles.cpp -o reasoning_profiles && mkdir -p ../outputs/tables && ./reasoning_profiles > ../outputs/tables/cpp_reasoning_profiles.csv; else echo "c++ not found; skipping."; fi

clean:
	rm -f reasoning_profiles
