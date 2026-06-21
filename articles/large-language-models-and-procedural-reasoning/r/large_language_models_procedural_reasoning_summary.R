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

audit_path <- file.path(tables_dir, "llm_reasoning_audit.csv")
summary_path <- file.path(tables_dir, "llm_audit_summary.csv")
if (!file.exists(audit_path)) stop(paste("Missing", audit_path, "Run the Python workflow first."))

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "llm_audit_status_counts.png"), width = 1000, height = 750)
status_counts <- table(audit$status)
barplot(status_counts, ylab = "Count", main = "LLM Procedural Reasoning Audit Status")
grid()
dev.off()

png(file.path(figures_dir, "llm_audit_score_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("procedural_score", "source_score", "risk_score", "overall_score")]))
barplot(score_matrix, beside = TRUE, names.arg = audit$case_id, las = 2, ylab = "Score", main = "LLM Audit Score Components")
legend("bottomright", legend = rownames(score_matrix), cex = 0.75, bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "llm_stakes_by_status.png"), width = 1000, height = 750)
stakes_status <- table(audit$stakes, audit$status)
barplot(stakes_status, beside = TRUE, ylab = "Count", main = "LLM Audit Status by Stakes Level")
legend("topright", legend = rownames(stakes_status), cex = 0.75, bty = "n")
grid()
dev.off()

r_summary <- data.frame(
  cases_reviewed = summary$cases_reviewed[1],
  cases_passed = summary$cases_passed[1],
  cases_requiring_review = summary$cases_requiring_review[1],
  cases_escalated = summary$cases_escalated[1],
  mean_overall_score = summary$mean_overall_score[1],
  diagnostic_note = "LLM outputs should be reviewed for source support, procedural adequacy, risk language, tool use, and escalation requirements."
)
write.csv(r_summary, file.path(tables_dir, "r_llm_reasoning_summary.csv"), row.names = FALSE)
print(r_summary)
