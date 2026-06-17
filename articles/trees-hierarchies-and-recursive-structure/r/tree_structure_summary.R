data <- read.csv("data/synthetic_tree_structure_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["hierarchy_fit"]] +
    0.12 * row[["recursive_clarity"]] +
    0.10 * row[["invariant_documentation"]] +
    0.10 * row[["traversal_support"]] +
    0.08 * row[["balance_awareness"]] +
    0.10 * row[["path_interpretability"]] +
    0.10 * row[["relationship_loss_control"]] +
    0.08 * row[["complexity_awareness"]] +
    0.10 * row[["representation_risk_documentation"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["hierarchy_fit"]],
    1 - row[["recursive_clarity"]],
    1 - row[["invariant_documentation"]],
    1 - row[["traversal_support"]],
    1 - row[["path_interpretability"]],
    1 - row[["relationship_loss_control"]],
    1 - row[["representation_risk_documentation"]],
    1 - row[["governance_readiness"]]
  ))
}

data$tree_structure_quality <- apply(data, 1, quality_score)
data$false_hierarchy_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_tree_structure_summary.csv", row.names = FALSE)

png("outputs/figures/r_tree_structure_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$tree_structure_quality, data$false_hierarchy_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Tree-structure quality", "False-hierarchy risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Tree Structure Quality vs. False-Hierarchy Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
