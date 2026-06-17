data <- read.csv("data/synthetic_abstraction_cases.csv", stringsAsFactors = FALSE)

score <- function(row) {
  100 * (
    0.12 * row[["representation_clarity"]] +
    0.10 * row[["scope_definition"]] +
    0.12 * row[["detail_preservation"]] +
    0.12 * row[["assumption_documentation"]] +
    0.10 * row[["testability"]] +
    0.12 * row[["interpretability"]] +
    0.08 * row[["reuse_safety"]] +
    0.08 * row[["uncertainty_visibility"]] +
    0.08 * row[["governance_readiness"]] +
    0.08 * row[["risk_awareness"]]
  )
}

risk <- function(row) {
  100 * mean(c(
    1 - row[["scope_definition"]],
    1 - row[["detail_preservation"]],
    1 - row[["assumption_documentation"]],
    1 - row[["interpretability"]],
    1 - row[["reuse_safety"]],
    1 - row[["uncertainty_visibility"]],
    1 - row[["governance_readiness"]],
    1 - row[["risk_awareness"]]
  ))
}

data$abstraction_score <- apply(data, 1, score)
data$abstraction_risk <- apply(data, 1, risk)
data$diagnostic <- ifelse(
  data$abstraction_score >= 80 & data$abstraction_risk <= 25,
  "strong abstraction",
  ifelse(data$abstraction_risk >= 55, "high abstraction risk", "review needed")
)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_abstraction_summary.csv", row.names = FALSE)

png("outputs/figures/r_abstraction_score_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$abstraction_score, data$abstraction_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Abstraction score", "Abstraction risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Abstraction Score vs. Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
