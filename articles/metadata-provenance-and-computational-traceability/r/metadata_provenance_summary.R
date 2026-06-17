data <- read.csv("data/synthetic_metadata_provenance_cases.csv", stringsAsFactors = FALSE)

quality_score <- function(row) {
  100 * (
    0.12 * row[["metadata_completeness"]] +
    0.10 * row[["source_clarity"]] +
    0.12 * row[["lineage_coverage"]] +
    0.10 * row[["version_control"]] +
    0.08 * row[["timestamp_quality"]] +
    0.10 * row[["schema_clarity"]] +
    0.10 * row[["integrity_checks"]] +
    0.10 * row[["access_governance"]] +
    0.10 * row[["reproducibility_support"]] +
    0.08 * row[["stewardship_readiness"]]
  )
}

risk_score <- function(row) {
  100 * mean(c(
    1 - row[["metadata_completeness"]],
    1 - row[["source_clarity"]],
    1 - row[["lineage_coverage"]],
    1 - row[["version_control"]],
    1 - row[["schema_clarity"]],
    1 - row[["integrity_checks"]],
    1 - row[["access_governance"]],
    1 - row[["reproducibility_support"]],
    1 - row[["stewardship_readiness"]]
  ))
}

data$traceability_quality <- apply(data, 1, quality_score)
data$traceability_risk <- apply(data, 1, risk_score)

dir.create("outputs/tables", recursive = TRUE, showWarnings = FALSE)
dir.create("outputs/figures", recursive = TRUE, showWarnings = FALSE)
write.csv(data, "outputs/tables/r_metadata_provenance_summary.csv", row.names = FALSE)

png("outputs/figures/r_traceability_quality_vs_risk.png", width = 1400, height = 800)
comparison <- rbind(data$traceability_quality, data$traceability_risk)
colnames(comparison) <- data$case_name
rownames(comparison) <- c("Traceability quality", "Traceability risk")
barplot(comparison, beside = TRUE, las = 2, ylim = c(0, 100), ylab = "Score", main = "Metadata and Provenance Quality vs. Traceability Risk")
legend("topleft", legend = rownames(comparison), pch = 15, bty = "n")
grid()
dev.off()

print(data)
