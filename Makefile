.PHONY: smoke python r sql list

smoke:
	@bash scripts/smoke_test.sh

python:
	@PYTHONPATH=python python3 -m algorithms_computational_reasoning.cli --demo all

r:
	@Rscript r/scripts/complexity_demo.R || true

sql:
	@sqlite3 outputs/acr_demo.sqlite < sql/schemas/article_index_schema.sql || true

list:
	@find articles -maxdepth 2 -name README.md | sort
