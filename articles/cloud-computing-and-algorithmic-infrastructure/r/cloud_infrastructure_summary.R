data <- read.csv("data/synthetic_cloud_infrastructure_cases.csv", stringsAsFactors = FALSE)
data$cloud_infrastructure_score <- 100 * (0.09*data$compute_design + 0.09*data$storage_governance + 0.08*data$network_design + 0.10*data$deployment_reproducibility + 0.11*data$observability + 0.11*data$identity_access_control + 0.08*data$cost_visibility + 0.08*data$scaling_policy + 0.10*data$resilience_design + 0.08*data$data_governance + 0.05*data$dependency_mapping + 0.03*data$communication_clarity)
data$cloud_infrastructure_risk <- 100 * rowMeans(1 - data[, c("storage_governance","deployment_reproducibility","observability","identity_access_control","cost_visibility","scaling_policy","resilience_design","data_governance","dependency_mapping")])
dir.create("outputs/tables", recursive=TRUE, showWarnings=FALSE)
dir.create("outputs/figures", recursive=TRUE, showWarnings=FALSE)
write.csv(data, "outputs/tables/r_cloud_infrastructure_summary.csv", row.names=FALSE)
png("outputs/figures/r_cloud_infrastructure_score_vs_risk.png", width=1500, height=850)
m <- rbind(data$cloud_infrastructure_score, data$cloud_infrastructure_risk)
colnames(m) <- data$case_name
rownames(m) <- c("Cloud infrastructure score", "Cloud infrastructure risk")
barplot(m, beside=TRUE, las=2, ylim=c(0,100), ylab="Score", main="Cloud Infrastructure Score vs. Risk")
legend("topleft", legend=rownames(m), pch=15, bty="n"); grid(); dev.off()
costs <- read.csv("data/synthetic_cloud_latency_cost.csv", stringsAsFactors=FALSE)
costs$total_latency_ms <- costs$compute_ms + costs$storage_ms + costs$network_ms + costs$queue_ms + costs$coordination_ms
costs$unit_cost <- (costs$compute_cost + costs$storage_cost + costs$network_cost + costs$managed_service_cost + costs$observability_cost) / costs$completed_work
write.csv(costs, "outputs/tables/r_cloud_latency_cost_summary.csv", row.names=FALSE)
print(data)
