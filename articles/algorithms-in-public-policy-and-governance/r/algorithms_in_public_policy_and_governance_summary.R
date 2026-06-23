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

audit_path <- file.path(tables_dir, "public_governance_audit.csv")
summary_path <- file.path(tables_dir, "public_governance_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "public_governance_readiness.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("rights_impact", "procedural_readiness_score", "governance_readiness_score", "public_value")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$use_case_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithms in Public Policy and Governance: Rights, Readiness, and Public Value")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "public_algorithmic_risk.png"), width = 1000, height = 750)
barplot(audit$public_algorithmic_risk_score,
        names.arg = audit$use_case_id,
        las = 2,
        ylab = "Public Algorithmic Risk Score",
        main = "Public Algorithmic Risk by Use Case")
grid()
dev.off()

r_summary <- data.frame(
  use_cases_reviewed = summary$use_cases_reviewed[1],
  use_cases_not_ready_for_deployment = summary$use_cases_not_ready_for_deployment[1],
  use_cases_requiring_governance_review = summary$use_cases_requiring_governance_review[1],
  use_cases_requiring_independent_oversight = summary$use_cases_requiring_independent_oversight[1],
  mean_procedural_readiness_score = summary$mean_procedural_readiness_score[1],
  mean_governance_readiness_score = summary$mean_governance_readiness_score[1],
  mean_public_algorithmic_risk_score = summary$mean_public_algorithmic_risk_score[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "Public algorithmic governance should connect rights impact, due process, transparency, human review, data quality, vendor accountability, appeals, monitoring, public value, and stop authority."
)

write.csv(r_summary, file.path(tables_dir, "r_public_governance_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
