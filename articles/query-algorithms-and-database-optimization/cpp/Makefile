.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 query_cost_model.cpp -o query_cost_model && mkdir -p ../outputs/tables && ./query_cost_model > ../outputs/tables/cpp_query_cost_model.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f query_cost_model
