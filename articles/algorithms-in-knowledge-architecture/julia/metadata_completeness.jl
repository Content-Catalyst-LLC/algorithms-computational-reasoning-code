present_fields = 11.0
required_fields = 12.0
score = present_fields / required_fields
println("metadata_completeness_score=", round(score, digits=4))
