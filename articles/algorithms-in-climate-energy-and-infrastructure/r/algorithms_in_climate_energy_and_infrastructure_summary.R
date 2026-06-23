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

audit_path <- file.path(tables_dir, "infrastructure_algorithm_risk_audit.csv")
summary_path <- file.path(tables_dir, "infrastructure_algorithm_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "infrastructure_algorithm_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("public_impact", "climate_exposure", "reliability_impact", "equity_readiness", "validation_readiness", "governance_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$system_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithms in Climate, Energy, and Infrastructure: Impact, Exposure, Reliability, and Governance")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "resilience_risk_by_system.png"), width = 1000, height = 750)
barplot(audit$resilience_risk_score,
        names.arg = audit$system_id,
        las = 2,
        ylab = "Resilience Risk Score",
        main = "Resilience Risk by Infrastructure System")
grid()
dev.off()

r_summary <- data.frame(
  systems_reviewed = summary$systems_reviewed[1],
  systems_requiring_governance_redesign = summary$systems_requiring_governance_redesign[1],
  systems_requiring_public_value_review = summary$systems_requiring_public_value_review[1],
  systems_requiring_reliability_review = summary$systems_requiring_reliability_review[1],
  systems_requiring_climate_equity_review = summary$systems_requiring_climate_equity_review[1],
  mean_resilience_risk_score = summary$mean_resilience_risk_score[1],
  mean_governance_score = summary$mean_governance_score[1],
  mean_impact_score = summary$mean_impact_score[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "Infrastructure algorithm governance should connect climate exposure, public impact, reliability impact, equity readiness, validation, monitoring, maintenance, uncertainty, human override, audit trails, and stop authority."
)

write.csv(r_summary, file.path(tables_dir, "r_infrastructure_algorithm_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
