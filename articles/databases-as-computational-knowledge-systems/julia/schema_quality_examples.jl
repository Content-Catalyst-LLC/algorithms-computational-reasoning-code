schema_quality(fields, keys, constraints, metadata, lineage) = 100 * (0.22*fields + 0.20*keys + 0.20*constraints + 0.20*metadata + 0.18*lineage)
println("test_name,value")
println("schema_quality_score,$(schema_quality(0.90,0.85,0.80,0.88,0.82))")
