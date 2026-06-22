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

audit_path <- file.path(tables_dir, "decision_science_audit.csv")
summary_path <- file.path(tables_dir, "decision_science_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "decision_science_scores.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("predicted_probability", "decision_support_readiness_score", "stakes")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$decision_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithms in Decision Science: Forecast, Readiness, and Stakes")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "expected_value_and_loss.png"), width = 1000, height = 750)
value_matrix <- t(as.matrix(audit[, c("expected_value_of_action", "expected_loss_if_no_action")]))
barplot(value_matrix,
        beside = TRUE,
        names.arg = audit$decision_id,
        las = 2,
        ylab = "Value or Loss",
        main = "Expected Value of Action and Expected Loss if No Action")
legend("topright",
       legend = rownames(value_matrix),
       cex = 0.75,
       bty = "n")
grid()
dev.off()

r_summary <- data.frame(
  decisions_reviewed = summary$decisions_reviewed[1],
  decisions_supporting_action = summary$decisions_supporting_action[1],
  decisions_escalated = summary$decisions_escalated[1],
  decisions_not_automated = summary$decisions_not_automated[1],
  mean_decision_support_readiness_score = summary$mean_decision_support_readiness_score[1],
  mean_expected_value_of_action = summary$mean_expected_value_of_action[1],
  mean_expected_loss_if_no_action = summary$mean_expected_loss_if_no_action[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "Decision support should connect forecasts, thresholds, uncertainty, review, contestability, monitoring, and stop authority."
)

write.csv(r_summary, file.path(tables_dir, "r_decision_science_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
