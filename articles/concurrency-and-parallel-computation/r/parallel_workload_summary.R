data <- read.csv("data/synthetic_concurrency_cases.csv", stringsAsFactors = FALSE)
data$concurrency_reliability_score <- 100 * (0.09*data$decomposition_clarity + 0.10*data$dependency_discipline + 0.11*data$shared_state_control + 0.09*data$synchronization_design + 0.09*data$idempotence + 0.08*data$deadlock_avoidance + 0.08*data$load_balancing + 0.10*data$observability + 0.09*data$failure_isolation + 0.07*data$reproducibility + 0.06*data$governance_review + 0.04*data$communication_clarity)
data$concurrency_risk <- 100 * rowMeans(1 - data[, c("dependency_discipline","shared_state_control","synchronization_design","idempotence","deadlock_avoidance","observability","failure_isolation","reproducibility","governance_review")])
dir.create("outputs/tables", recursive=TRUE, showWarnings=FALSE)
dir.create("outputs/figures", recursive=TRUE, showWarnings=FALSE)
write.csv(data, "outputs/tables/r_parallel_workload_summary.csv", row.names=FALSE)
png("outputs/figures/r_concurrency_reliability_vs_risk.png", width=1500, height=850)
m <- rbind(data$concurrency_reliability_score, data$concurrency_risk)
colnames(m) <- data$case_name
rownames(m) <- c("Concurrency reliability", "Concurrency risk")
barplot(m, beside=TRUE, las=2, ylim=c(0,100), ylab="Score", main="Concurrency Reliability vs. Risk")
legend("topleft", legend=rownames(m), pch=15, bty="n"); grid(); dev.off()
perf <- read.csv("data/synthetic_parallel_performance.csv", stringsAsFactors=FALSE)
perf$observed_speedup <- perf$sequential_time / perf$parallel_time
perf$observed_efficiency <- perf$observed_speedup / perf$processors
write.csv(perf, "outputs/tables/r_parallel_performance_examples.csv", row.names=FALSE)
print(data)
