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

audit_path <- file.path(tables_dir, "explanation_audit.csv")
summary_path <- file.path(tables_dir, "explanation_audit_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "explanation_quality_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("faithfulness", "stability", "understandability", "actionability", "uncertainty_communication", "contestability")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$case_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Transparency, Explainability, and Interpretability Components")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "explanation_risk_by_case.png"), width = 1000, height = 750)
barplot(audit$explanation_risk_score,
        names.arg = audit$case_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Explanation Risk Score",
        main = "Explanation Risk by Case")
grid()
dev.off()

r_summary <- data.frame(
  cases_reviewed = summary$cases_reviewed[1],
  cases_passed = summary$cases_passed[1],
  cases_requiring_review = summary$cases_requiring_review[1],
  cases_escalated = summary$cases_escalated[1],
  mean_explanation_quality_score = summary$mean_explanation_quality_score[1],
  mean_transparency_capacity_score = summary$mean_transparency_capacity_score[1],
  mean_accountability_capacity_score = summary$mean_accountability_capacity_score[1],
  mean_explanation_risk_score = summary$mean_explanation_risk_score[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Explanation review should connect faithfulness, stability, understandability, actionability, uncertainty, documentation, contestability, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_explanation_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
