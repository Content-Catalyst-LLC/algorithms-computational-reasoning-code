data <- read.csv("data/synthetic_type_representation_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["representation_clarity"]] +
    0.12 * row[["constraint_strength"]] +
    0.10 * row[["missingness_handling"]] +
    0.10 * row[["boundary_validation"]] +
    0.10 * row[["domain_fidelity"]] +
    0.10 * row[["error_specificity"]] +
    0.10 * row[["type_coverage"]] +
    0.08 * row[["interoperability"]] +
    0.10 * row[["testability"]] +
    0.08 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["representation_clarity"]],
    1 - row[["constraint_strength"]],
    1 - row[["missingness_handling"]],
    1 - row[["boundary_validation"]],
    1 - row[["domain_fidelity"]],
    1 - row[["error_specificity"]],
    1 - row[["type_coverage"]],
    1 - row[["governance_readiness"]]
  ))
}

data$type_quality <- apply(data, 1, quality_score)
data$type_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_type_representation_summary.csv", row.names = FALSE)

png("outputs/figures/r_type_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$type_quality, data$type_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Type quality", "Type risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Type Quality vs. Representation Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
