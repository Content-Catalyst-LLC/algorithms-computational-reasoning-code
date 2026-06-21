known = Set(["traceable_system", "reviewable_system", "hybrid_system"])
required = Set(["traceable_system", "reviewable_system", "hybrid_system", "requires_escalation_review"])
score = length(intersect(known, required)) / length(required)
println("symbolic_constraint_score=", round(score, digits=4))
