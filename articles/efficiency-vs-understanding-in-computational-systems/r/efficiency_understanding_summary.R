data <- read.csv("data/synthetic_efficiency_understanding_cases.csv", stringsAsFactors = FALSE)
data$efficiency_score <- 100 * (0.30*data$performance_gain + 0.25*data$memory_gain + 0.25*data$cost_gain + 0.20*data$energy_awareness)
data$understanding_score <- 100 * (0.12*data$readability + 0.12*data$debuggability + 0.12*data$explainability + 0.12*data$observability + 0.12*data$auditability + 0.10*data$reproducibility + 0.12*data$maintainability + 0.10*data$governance_readiness + 0.08*data$communication_clarity)
data$responsible_efficiency_score <- 0.5*data$efficiency_score + 0.5*data$understanding_score
data$tradeoff_risk <- pmax(data$efficiency_score - data$understanding_score, 0) * 0.65 + (100 - 100*rowMeans(data[, c("auditability","governance_readiness","communication_clarity","reproducibility")])) * 0.35
dir.create("outputs/tables", recursive=TRUE, showWarnings=FALSE)
dir.create("outputs/figures", recursive=TRUE, showWarnings=FALSE)
write.csv(data, "outputs/tables/r_efficiency_understanding_summary.csv", row.names=FALSE)
png("outputs/figures/r_efficiency_understanding_tradeoff.png", width=1500, height=850)
m <- rbind(data$efficiency_score, data$understanding_score, data$responsible_efficiency_score, data$tradeoff_risk)
colnames(m) <- data$case_name
rownames(m) <- c("Efficiency", "Understanding", "Responsible efficiency", "Trade-off risk")
barplot(m, beside=TRUE, las=2, ylim=c(0,100), ylab="Score", main="Efficiency, Understanding, and Trade-off Risk")
legend("topleft", legend=rownames(m), pch=15, bty="n"); grid(); dev.off()
print(data)
