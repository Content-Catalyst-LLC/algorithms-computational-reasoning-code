data <- read.csv("data/synthetic_graph_relationship_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["edge_meaning_clarity"]] +
    0.10 * row[["node_definition_clarity"]] +
    0.10 * row[["direction_clarity"]] +
    0.08 * row[["weight_interpretability"]] +
    0.10 * row[["path_validity"]] +
    0.10 * row[["connectivity_evidence"]] +
    0.10 * row[["metadata_provenance"]] +
    0.10 * row[["algorithm_fit"]] +
    0.10 * row[["representation_risk_documentation"]] +
    0.10 * row[["governance_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["edge_meaning_clarity"]],
    1 - row[["node_definition_clarity"]],
    1 - row[["direction_clarity"]],
    1 - row[["weight_interpretability"]],
    1 - row[["path_validity"]],
    1 - row[["metadata_provenance"]],
    1 - row[["representation_risk_documentation"]],
    1 - row[["governance_readiness"]]
  ))
}

data$graph_reasoning_quality <- apply(data, 1, quality_score)
data$relationship_overclaim_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_graph_relationship_summary.csv", row.names = FALSE)

png("outputs/figures/r_graph_reasoning_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$graph_reasoning_quality, data$relationship_overclaim_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Graph-reasoning quality", "Relationship-overclaim risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Graph Reasoning Quality vs. Relationship-Overclaim Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
