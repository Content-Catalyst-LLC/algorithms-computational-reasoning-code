traceability_quality('Research dataset repository', 89.10).
traceability_quality('AI model registry', 87.00).
traceability_quality('Institutional case workflow', 87.08).
traceability_quality('Knowledge library article system', 83.68).

used('cleaning-script-a', 'raw-data-v1').
was_generated_by('analysis-table-v1', 'cleaning-script-a').
was_derived_from('published-chart-v1', 'raw-data-v1').
traceable(X) :- traceability_quality(X, _).
