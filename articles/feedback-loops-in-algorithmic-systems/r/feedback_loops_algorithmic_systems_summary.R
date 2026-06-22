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

audit_path <- file.path(tables_dir, "feedback_loop_audit.csv")
summary_path <- file.path(tables_dir, "feedback_audit_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "feedback_loop_risk_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("amplification", "exposure_concentration", "intervention_influence", "drift", "recursive_data", "feedback_risk_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$case_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithmic Feedback Loop Risk Components")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "feedback_audit_status_counts.png"), width = 1000, height = 750)
status_counts <- table(audit$status)
barplot(status_counts,
        ylab = "Count",
        main = "Feedback Loop Audit Status Counts")
grid()
dev.off()

r_summary <- data.frame(
  feedback_cases_reviewed = summary$feedback_cases_reviewed[1],
  cases_passed = summary$cases_passed[1],
  cases_requiring_review = summary$cases_requiring_review[1],
  cases_escalated = summary$cases_escalated[1],
  mean_feedback_risk_score = summary$mean_feedback_risk_score[1],
  mean_drift = summary$mean_drift[1],
  drift_scenarios = summary$drift_scenarios[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Feedback-loop governance should review exposure, amplification, intervention effects, drift, recursive data, correction, monitoring, and update boundaries."
)

write.csv(r_summary, file.path(tables_dir, "r_feedback_loop_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
