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

audit_path <- file.path(tables_dir, "human_review_audit.csv")
summary_path <- file.path(tables_dir, "human_review_audit_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "human_review_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("review_capacity_score", "reliance_score", "override_rate", "escalation_capacity", "contestability", "governance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$context_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Human-in-the-Loop and Human Judgment Components")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "review_risk_by_context.png"), width = 1000, height = 750)
barplot(audit$review_risk_score,
        names.arg = audit$context_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Review Risk Score",
        main = "Meaningful Human Review Risk by Context")
grid()
dev.off()

r_summary <- data.frame(
  contexts_reviewed = summary$contexts_reviewed[1],
  contexts_passed = summary$contexts_passed[1],
  contexts_requiring_review = summary$contexts_requiring_review[1],
  contexts_escalated = summary$contexts_escalated[1],
  mean_review_capacity_score = summary$mean_review_capacity_score[1],
  mean_reliance_score = summary$mean_reliance_score[1],
  mean_override_rate = summary$mean_override_rate[1],
  mean_judgment_capacity_score = summary$mean_judgment_capacity_score[1],
  mean_review_risk_score = summary$mean_review_risk_score[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Human review should connect time, information, authority, training, protection, reliance, overrides, escalation, contestability, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_human_review_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
