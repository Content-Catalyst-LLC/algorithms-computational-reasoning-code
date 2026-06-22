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

audit_path <- file.path(tables_dir, "risk_governance_audit.csv")
summary_path <- file.path(tables_dir, "risk_governance_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "risk_governance_scores.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("inherent_risk_score", "governance_readiness_score", "control_effectiveness", "residual_risk_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$risk_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithmic Risk Management and AI Governance Scores")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "residual_risk_by_system.png"), width = 1000, height = 750)
barplot(audit$residual_risk_score,
        names.arg = audit$system,
        las = 2,
        ylim = c(0, 1),
        ylab = "Residual Risk Score",
        main = "Residual Risk by Algorithmic System")
grid()
dev.off()

r_summary <- data.frame(
  risks_reviewed = summary$risks_reviewed[1],
  risks_controlled = summary$risks_controlled[1],
  risks_requiring_review = summary$risks_requiring_review[1],
  risks_escalated = summary$risks_escalated[1],
  mean_inherent_risk_score = summary$mean_inherent_risk_score[1],
  mean_governance_readiness_score = summary$mean_governance_readiness_score[1],
  mean_residual_risk_score = summary$mean_residual_risk_score[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "AI governance should connect risk severity, likelihood, detectability, controls, ownership, monitoring, contestability, remediation, and stop authority."
)

write.csv(r_summary, file.path(tables_dir, "r_risk_governance_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
