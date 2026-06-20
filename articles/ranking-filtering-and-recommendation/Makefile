.PHONY: smoke all python r calculators clean

smoke: python calculators

all: python calculators r

python:
	PYTHONPATH=python python3 python/ranking_recommendation/audit.py
	PYTHONPATH=python python3 python/ranking_recommendation/cli.py >/tmp/ranking_cli_output.json

calculators:
	bash calculators/run_calculator_smoke_tests.sh

r:
	Rscript r/ranking_filtering_recommendation_summary.R || true

clean:
	rm -rf outputs/tables/*.csv outputs/json/*.json outputs/figures/*.png outputs/logs/*.log
