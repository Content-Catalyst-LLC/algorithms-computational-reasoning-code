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

audit_path <- file.path(tables_dir, "agent_tool_use_audit.csv")
summary_path <- file.path(tables_dir, "agent_audit_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "agent_action_status_counts.png"), width = 1000, height = 750)
status_counts <- table(audit$status)
barplot(status_counts,
        ylab = "Count",
        main = "Agent Action Status Counts")
grid()
dev.off()

png(file.path(figures_dir, "agent_tool_risk_by_step.png"), width = 1100, height = 800)
barplot(audit$tool_risk,
        names.arg = paste(audit$step, audit$tool, sep = ": "),
        las = 2,
        ylab = "Tool risk",
        main = "Agent Tool Risk by Workflow Step")
abline(h = 0.65, lty = 2)
grid()
dev.off()

png(file.path(figures_dir, "agent_approval_violations.png"), width = 1100, height = 800)
barplot(audit$approval_violation,
        names.arg = paste(audit$step, audit$tool, sep = ": "),
        las = 2,
        ylab = "Approval violation",
        main = "Agent Approval Violations by Step")
grid()
dev.off()

r_summary <- data.frame(
  actions_reviewed = summary$actions_reviewed[1],
  actions_passed = summary$actions_passed[1],
  actions_escalated = summary$actions_escalated[1],
  actions_blocked = summary$actions_blocked[1],
  approval_violations = summary$approval_violations[1],
  untrusted_instruction_events = summary$untrusted_instruction_events[1],
  mean_tool_risk = summary$mean_tool_risk[1],
  recommended_autonomy_level = summary$recommended_autonomy_level[1],
  diagnostic_note = "Agent reliability should be reviewed through tool permissions, approval gates, escalation thresholds, prompt-injection controls, and workflow logs."
)

write.csv(r_summary, file.path(tables_dir, "r_agent_reliability_summary.csv"), row.names = FALSE)
print(r_summary)
