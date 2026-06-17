data <- read.csv("data/synthetic_computability_boundary_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.10 * row[["procedure_definition"]] +
    0.10 * row[["input_domain_clarity"]] +
    0.12 * row[["decision_status_clarity"]] +
    0.12 * row[["termination_guarantee"]] +
    0.10 * row[["recognizability_status"]] +
    0.10 * row[["reduction_awareness"]] +
    0.10 * row[["approximation_honesty"]] +
    0.10 * row[["automation_scope_clarity"]] +
    0.08 * row[["traceability"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["decision_status_clarity"]],
    1 - row[["termination_guarantee"]],
    1 - row[["recognizability_status"]],
    1 - row[["reduction_awareness"]],
    1 - row[["approximation_honesty"]],
    1 - row[["automation_scope_clarity"]],
    1 - row[["traceability"]],
    1 - row[["governance_readiness"]]
  ))
}

data$computability_boundary_quality <- apply(data, 1, quality_score)
data$procedural_overclaim_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_computability_boundary_summary.csv", row.names = FALSE)

png("outputs/figures/r_computability_boundary_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$computability_boundary_quality, data$procedural_overclaim_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Computability-boundary quality", "Procedural-overclaim risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Computability Boundary Quality vs. Procedural Overclaim Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
