args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

audit_path <- file.path(tables_dir, "financial_algorithm_risk_audit.csv")
summary_path <- file.path(tables_dir, "financial_algorithm_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "financial_algorithm_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("market_impact", "consumer_impact", "model_risk", "liquidity_risk", "governance_readiness_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$system_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithms in Finance, Markets, and Risk: Impact, Model Risk, and Governance")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "financial_algorithm_risk_by_system.png"), width = 1000, height = 750)
barplot(audit$financial_algorithm_risk_score,
        names.arg = audit$system_id,
        las = 2,
        ylab = "Financial Algorithm Risk Score",
        main = "Financial Algorithm Risk by System")
grid()
dev.off()

r_summary <- data.frame(
  systems_reviewed = summary$systems_reviewed[1],
  systems_requiring_control_redesign = summary$systems_requiring_control_redesign[1],
  systems_requiring_consumer_protection_review = summary$systems_requiring_consumer_protection_review[1],
  systems_requiring_market_stability_review = summary$systems_requiring_market_stability_review[1],
  systems_requiring_model_governance_review = summary$systems_requiring_model_governance_review[1],
  mean_financial_algorithm_risk_score = summary$mean_financial_algorithm_risk_score[1],
  mean_governance_readiness_score = summary$mean_governance_readiness_score[1],
  mean_impact_score = summary$mean_impact_score[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "Financial algorithm governance should connect market impact, consumer impact, model risk, validation, transparency, human review, monitoring, liquidity risk, audit trails, stress testing, and stop authority."
)

write.csv(r_summary, file.path(tables_dir, "r_financial_algorithm_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
