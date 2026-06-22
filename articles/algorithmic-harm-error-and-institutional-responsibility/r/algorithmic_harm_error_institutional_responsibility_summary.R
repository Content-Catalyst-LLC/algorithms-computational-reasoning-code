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

audit_path <- file.path(tables_dir, "harm_responsibility_audit.csv")
summary_path <- file.path(tables_dir, "harm_responsibility_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "harm_responsibility_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("harm_risk_score", "responsibility_capacity", "remediation_gap", "contestability", "monitoring", "repair")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$case_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithmic Harm and Institutional Responsibility Components")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "harm_responsibility_status_counts.png"), width = 1000, height = 750)
status_counts <- table(audit$status)
barplot(status_counts,
        ylab = "Count",
        main = "Harm and Responsibility Audit Status Counts")
grid()
dev.off()

r_summary <- data.frame(
  cases_reviewed = summary$cases_reviewed[1],
  cases_passed = summary$cases_passed[1],
  cases_requiring_review = summary$cases_requiring_review[1],
  cases_escalated = summary$cases_escalated[1],
  mean_harm_risk_score = summary$mean_harm_risk_score[1],
  mean_responsibility_capacity = summary$mean_responsibility_capacity[1],
  mean_remediation_gap = summary$mean_remediation_gap[1],
  harm_taxonomy_entries = summary$harm_taxonomy_entries[1],
  incident_fields_required = summary$incident_fields_required[1],
  diagnostic_note = "Algorithmic harm review should connect technical error to severity, exposure, contestability, institutional ownership, monitoring, appeal, repair, governance, and remediation."
)

write.csv(r_summary, file.path(tables_dir, "r_harm_responsibility_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
