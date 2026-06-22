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

audit_path <- file.path(tables_dir, "accountability_audit.csv")
summary_path <- file.path(tables_dir, "accountability_audit_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "accountability_capacity_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("audit_completeness_score", "documentation", "provenance", "reviewability", "contestability", "remediation", "governance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$system_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithmic Accountability and Audit Trail Components")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "reconstruction_risk_by_system.png"), width = 1000, height = 750)
barplot(audit$reconstruction_risk_score,
        names.arg = audit$system_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Reconstruction Risk Score",
        main = "Decision Reconstruction Risk by System")
grid()
dev.off()

r_summary <- data.frame(
  systems_reviewed = summary$systems_reviewed[1],
  systems_passed = summary$systems_passed[1],
  systems_requiring_review = summary$systems_requiring_review[1],
  systems_escalated = summary$systems_escalated[1],
  mean_audit_completeness_score = summary$mean_audit_completeness_score[1],
  mean_accountability_capacity_score = summary$mean_accountability_capacity_score[1],
  mean_reconstruction_risk_score = summary$mean_reconstruction_risk_score[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Accountability review should connect audit completeness, documentation, provenance, decision logs, contestability, remediation, ownership, and reconstruction risk."
)

write.csv(r_summary, file.path(tables_dir, "r_accountability_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
