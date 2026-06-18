data <- read.csv("data/synthetic_data_quality_cases.csv", stringsAsFactors = FALSE)
data$data_quality_score <- 100 * (0.10*data$completeness + 0.09*data$validity + 0.08*data$freshness + 0.10*data$provenance + 0.08*data$schema_stability + 0.10*data$representativeness + 0.09*data$missingness_documentation + 0.08*data$imputation_discipline + 0.10*data$validation_coverage + 0.07*data$governance_review + 0.06*data$uncertainty_communication + 0.05*data$fitness_for_purpose)
data$computational_judgment_risk <- 100 * rowMeans(1 - data[, c("completeness","provenance","representativeness","missingness_documentation","imputation_discipline","validation_coverage","governance_review","uncertainty_communication","fitness_for_purpose")])
dir.create("outputs/tables", recursive=TRUE, showWarnings=FALSE)
dir.create("outputs/figures", recursive=TRUE, showWarnings=FALSE)
write.csv(data, "outputs/tables/r_missingness_quality_summary.csv", row.names=FALSE)
png("outputs/figures/r_data_quality_vs_judgment_risk.png", width=1500, height=850)
m <- rbind(data$data_quality_score, data$computational_judgment_risk)
colnames(m) <- data$case_name
rownames(m) <- c("Data quality", "Computational judgment risk")
barplot(m, beside=TRUE, las=2, ylim=c(0,100), ylab="Score", main="Data Quality vs. Computational Judgment Risk")
legend("topleft", legend=rownames(m), pch=15, bty="n"); grid(); dev.off()
missingness_path <- "outputs/tables/missingness_profile_examples.csv"
if (file.exists(missingness_path)) {
  missingness <- read.csv(missingness_path, stringsAsFactors=FALSE)
  write.csv(missingness[order(-missingness$missingness_rate), ], "outputs/tables/r_missingness_profile_ranked.csv", row.names=FALSE)
}
print(data)
