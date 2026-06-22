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

audit_path <- file.path(tables_dir, "algorithmic_non_use_audit.csv")
summary_path <- file.path(tables_dir, "algorithmic_non_use_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "non_use_review_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("target_legitimacy", "data_legitimacy", "contestability", "human_judgment", "governance_capacity", "repairability", "non_use_pressure_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$use_case,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithmic Non-Use Review Components")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.66,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "non_use_pressure_by_case.png"), width = 1000, height = 750)
barplot(audit$non_use_pressure_score,
        names.arg = audit$use_case,
        las = 2,
        ylim = c(0, 1),
        ylab = "Non-Use Pressure Score",
        main = "Non-Use Pressure by Use Case")
grid()
dev.off()

r_summary <- data.frame(
  use_cases_reviewed = summary$use_cases_reviewed[1],
  use_cases_passed = summary$use_cases_passed[1],
  use_cases_requiring_review = summary$use_cases_requiring_review[1],
  use_cases_refused = summary$use_cases_refused[1],
  mean_responsible_use_readiness_score = summary$mean_responsible_use_readiness_score[1],
  mean_non_use_pressure_score = summary$mean_non_use_pressure_score[1],
  non_use_criteria = summary$non_use_criteria[1],
  diagnostic_note = "Algorithmic non-use review should connect target legitimacy, data legitimacy, contestability, human judgment, governance capacity, repairability, stakes, irreversibility, and proxy legitimacy."
)

write.csv(r_summary, file.path(tables_dir, "r_algorithmic_non_use_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
