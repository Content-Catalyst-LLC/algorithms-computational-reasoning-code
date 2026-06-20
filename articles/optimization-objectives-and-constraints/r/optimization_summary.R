data <- read.csv("data/synthetic_optimization_cases.csv", stringsAsFactors = FALSE)
data$optimization_score <- 100 * (0.11*data$objective_clarity + 0.11*data$constraint_documentation + 0.10*data$feasible_set_clarity + 0.09*data$data_quality + 0.09*data$uncertainty_handling + 0.08*data$sensitivity_review + 0.10*data$tradeoff_transparency + 0.09*data$fairness_review + 0.08*data$robustness_review + 0.07*data$traceability + 0.06*data$governance_review + 0.02*data$communication_clarity)
data$optimization_risk <- 100 * rowMeans(1 - data[, c("objective_clarity","constraint_documentation","feasible_set_clarity","data_quality","uncertainty_handling","sensitivity_review","tradeoff_transparency","fairness_review","robustness_review","traceability","governance_review")])
dir.create("outputs/tables", recursive=TRUE, showWarnings=FALSE)
dir.create("outputs/figures", recursive=TRUE, showWarnings=FALSE)
write.csv(data, "outputs/tables/r_optimization_summary.csv", row.names=FALSE)
png("outputs/figures/r_optimization_score_vs_risk.png", width=1500, height=850)
m <- rbind(data$optimization_score, data$optimization_risk)
colnames(m) <- data$case_name
rownames(m) <- c("Optimization score", "Optimization risk")
barplot(m, beside=TRUE, las=2, ylim=c(0,100), ylab="Score", main="Optimization Score vs. Risk")
legend("topleft", legend=rownames(m), pch=15, bty="n"); grid(); dev.off()

calc <- read.csv("data/synthetic_optimization_calculator_inputs.csv", stringsAsFactors=FALSE)
parse_nums <- function(x) as.numeric(strsplit(x, ";")[[1]])
calc$linear_objective <- mapply(function(cfs, vals) sum(parse_nums(cfs) * parse_nums(vals)), calc$coefficients, calc$decision_values)
calc$constraint_margin <- calc$limit - calc$observed_value
calc$penalty_objective <- calc$base_objective + calc$penalty_weight * calc$penalty
calc$normalized_tradeoff_score <- (0.35*(1 - calc$cost_score)) + (0.40*calc$quality_score) + (0.25*(1 - calc$risk_score))
write.csv(calc, "outputs/tables/r_optimization_calculator_input_summary.csv", row.names=FALSE)
print(data)
