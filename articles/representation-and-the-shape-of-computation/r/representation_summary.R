data <- read.csv("data/synthetic_representation_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["structural_fidelity"]] +
    0.12 * row[["operation_fit"]] +
    0.10 * row[["validation_discipline"]] +
    0.10 * row[["information_loss_control"]] +
    0.10 * row[["traceability"]] +
    0.10 * row[["interpretability"]] +
    0.08 * row[["retrieval_support"]] +
    0.08 * row[["transformation_readiness"]] +
    0.10 * row[["risk_documentation"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["structural_fidelity"]],
    1 - row[["operation_fit"]],
    1 - row[["validation_discipline"]],
    1 - row[["information_loss_control"]],
    1 - row[["traceability"]],
    1 - row[["interpretability"]],
    1 - row[["risk_documentation"]],
    1 - row[["governance_readiness"]]
  ))
}

data$representation_quality <- apply(data, 1, quality_score)
data$representation_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_representation_summary.csv", row.names = FALSE)

png("outputs/figures/r_representation_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$representation_quality, data$representation_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Representation quality", "Representation risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Representation Quality vs. Representation Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
