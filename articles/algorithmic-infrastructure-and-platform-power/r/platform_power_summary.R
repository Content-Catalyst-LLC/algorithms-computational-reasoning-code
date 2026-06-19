data <- read.csv("data/synthetic_platform_power_cases.csv", stringsAsFactors = FALSE)
data$platform_power_risk <- 100 * (
  0.11*data$access_dependence + 0.11*data$visibility_dependence + 0.10*data$api_dependence +
  0.10*data$data_dependence + 0.09*data$cost_dependence + 0.11*data$switching_difficulty +
  0.10*(1-data$interoperability) + 0.09*(1-data$transparency) + 0.08*(1-data$auditability) +
  0.06*(1-data$appeal_mechanism) + 0.04*(1-data$governance_review) + 0.01*(1-data$communication_clarity)
)
data$platform_accountability_score <- 100 * (
  0.18*data$interoperability + 0.18*data$transparency + 0.17*data$auditability +
  0.14*data$appeal_mechanism + 0.17*data$governance_review + 0.16*data$communication_clarity
)
dir.create("outputs/tables", recursive=TRUE, showWarnings=FALSE)
dir.create("outputs/figures", recursive=TRUE, showWarnings=FALSE)
write.csv(data, "outputs/tables/r_platform_power_summary.csv", row.names=FALSE)
png("outputs/figures/r_platform_power_risk_vs_accountability.png", width=1500, height=850)
m <- rbind(data$platform_power_risk, data$platform_accountability_score)
colnames(m) <- data$case_name
rownames(m) <- c("Platform power risk", "Platform accountability score")
barplot(m, beside=TRUE, las=2, ylim=c(0,100), ylab="Score", main="Platform Power Risk vs. Accountability")
legend("topleft", legend=rownames(m), pch=15, bty="n"); grid(); dev.off()
metrics <- read.csv("data/synthetic_platform_dependency_metrics.csv", stringsAsFactors=FALSE)
metrics$dependency_score <- 100 * (0.22*metrics$access_dependence + 0.22*metrics$visibility_dependence + 0.18*metrics$cost_dependence + 0.24*metrics$switching_difficulty + 0.14*metrics$evidence_dependence)
metrics$switching_cost <- metrics$migration + metrics$rebuild + metrics$training + metrics$downtime + metrics$lost_network
metrics$api_dependency_ratio <- metrics$platform_requests / metrics$total_requests
metrics$visibility_share <- metrics$actor_exposure / metrics$total_exposure
write.csv(metrics, "outputs/tables/r_platform_dependency_metrics_summary.csv", row.names=FALSE)
print(data)
