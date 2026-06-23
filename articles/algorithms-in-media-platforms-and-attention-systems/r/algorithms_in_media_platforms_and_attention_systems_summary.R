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

audit_path <- file.path(tables_dir, "attention_system_audit.csv")
summary_path <- file.path(tables_dir, "attention_system_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "attention_system_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("engagement_pressure", "creator_impact", "public_knowledge_impact", "user_control", "governance_readiness_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$system_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithms in Media Platforms: Attention Risk and Governance")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "platform_risk_by_system.png"), width = 1000, height = 750)
barplot(audit$platform_risk_score,
        names.arg = audit$system_id,
        las = 2,
        ylab = "Platform Risk Score",
        main = "Platform Risk by Attention System")
grid()
dev.off()

r_summary <- data.frame(
  systems_reviewed = summary$systems_reviewed[1],
  systems_requiring_redesign = summary$systems_requiring_redesign[1],
  systems_requiring_public_interest_review = summary$systems_requiring_public_interest_review[1],
  systems_requiring_governance_review = summary$systems_requiring_governance_review[1],
  mean_attention_risk_score = summary$mean_attention_risk_score[1],
  mean_governance_readiness_score = summary$mean_governance_readiness_score[1],
  mean_platform_risk_score = summary$mean_platform_risk_score[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "Media platform governance should connect engagement pressure, creator impact, public knowledge, transparency, contestability, moderation, user control, monitoring, and stop authority."
)

write.csv(r_summary, file.path(tables_dir, "r_attention_system_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
