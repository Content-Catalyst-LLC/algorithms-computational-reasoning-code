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

audit_path <- file.path(tables_dir, "systems_modeling_audit.csv")
summary_path <- file.path(tables_dir, "systems_modeling_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "systems_modeling_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("feedback_strength", "network_dependency", "scenario_uncertainty", "resilience", "model_readiness_score", "system_vulnerability_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$scenario_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithms in Systems Modeling: Components and Readiness")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.66,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "systems_modeling_risk_by_scenario.png"), width = 1000, height = 750)
barplot(audit$system_modeling_risk_score,
        names.arg = audit$scenario_id,
        las = 2,
        ylab = "Systems Modeling Risk Score",
        main = "Systems Modeling Risk by Scenario")
grid()
dev.off()

r_summary <- data.frame(
  scenarios_reviewed = summary$scenarios_reviewed[1],
  scenarios_for_escalation = summary$scenarios_for_escalation[1],
  scenarios_requiring_governance_review = summary$scenarios_requiring_governance_review[1],
  scenarios_not_ready_for_decision_use = summary$scenarios_not_ready_for_decision_use[1],
  mean_system_vulnerability_score = summary$mean_system_vulnerability_score[1],
  mean_model_readiness_score = summary$mean_model_readiness_score[1],
  mean_system_modeling_risk_score = summary$mean_system_modeling_risk_score[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "Systems modeling review should connect feedback, network dependency, scenario uncertainty, resilience, calibration, documentation, governance, and decision use."
)

write.csv(r_summary, file.path(tables_dir, "r_systems_modeling_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
