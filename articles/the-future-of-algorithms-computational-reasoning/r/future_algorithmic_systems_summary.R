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

map_path <- file.path(tables_dir, "future_algorithmic_systems_map.csv")
summary_path <- file.path(tables_dir, "future_algorithmic_systems_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

future_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "future_algorithmic_systems_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(future_map[, c("technical_capability", "institutional_consequence", "uncertainty", "automation_level", "opacity", "contestability_need", "governance_maturity", "human_judgment_requirement", "failure_severity", "deployment_readiness")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = future_map$domain_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "The Future of Algorithms and Computational Reasoning")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "future_risk_vs_readiness.png"), width = 950, height = 750)
plot(future_map$readiness_score,
     future_map$risk_score,
     xlim = c(0, 1),
     ylim = c(0, 1),
     xlab = "Readiness Score",
     ylab = "Risk Score",
     main = "Future Algorithmic Systems: Risk vs Readiness")
text(future_map$readiness_score,
     future_map$risk_score,
     labels = future_map$domain_id,
     pos = 4,
     cex = 0.65)
grid()
dev.off()

r_summary <- data.frame(
  domains_reviewed = summary$domains_reviewed[1],
  high_risk_governance_gaps = summary$high_risk_governance_gaps[1],
  high_risk_requires_governance = summary$high_risk_requires_governance[1],
  cautious_deployment_possible = summary$cautious_deployment_possible[1],
  further_review_needed = summary$further_review_needed[1],
  mean_risk_score = summary$mean_risk_score[1],
  mean_readiness_score = summary$mean_readiness_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Future algorithmic systems require technical capability, governance maturity, contestability, evidence discipline, human judgment, and institutional responsibility."
)

write.csv(r_summary, file.path(tables_dir, "r_future_algorithmic_systems_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
