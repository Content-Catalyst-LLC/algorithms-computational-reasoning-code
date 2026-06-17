.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 graph_relationship_audit.cpp -o graph_relationship_audit && mkdir -p ../outputs/tables && ./graph_relationship_audit > ../outputs/tables/cpp_graph_relationship_audit.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f graph_relationship_audit
