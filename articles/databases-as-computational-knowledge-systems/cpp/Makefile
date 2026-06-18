.PHONY: run clean
run:
	@if command -v c++ >/dev/null 2>&1; then c++ -O2 -std=c++17 database_knowledge_audit.cpp -o database_knowledge_audit && mkdir -p ../outputs/tables && ./database_knowledge_audit > ../outputs/tables/cpp_database_checks.csv; else echo "c++ not found; skipping."; fi
clean:
	rm -f database_knowledge_audit
