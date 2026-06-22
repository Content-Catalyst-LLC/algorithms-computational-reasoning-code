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

audit_path <- file.path(tables_dir, "knowledge_architecture_audit.csv")
summary_path <- file.path(tables_dir, "knowledge_architecture_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "knowledge_architecture_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("metadata_completeness", "taxonomy_fit", "search_readiness", "link_quality", "recommendation_quality", "governance_readiness_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$object_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithms in Knowledge Architecture: Components and Governance")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.66,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "knowledge_architecture_risk.png"), width = 1000, height = 750)
risk_matrix <- t(as.matrix(audit[, c("maintenance_risk_score", "representation_risk")]))
barplot(risk_matrix,
        beside = TRUE,
        names.arg = audit$object_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Risk Score",
        main = "Maintenance and Representation Risk")
legend("topright",
       legend = rownames(risk_matrix),
       cex = 0.75,
       bty = "n")
grid()
dev.off()

r_summary <- data.frame(
  objects_reviewed = summary$objects_reviewed[1],
  objects_ready = summary$objects_ready[1],
  objects_requiring_editorial_review = summary$objects_requiring_editorial_review[1],
  objects_requiring_metadata_or_link_review = summary$objects_requiring_metadata_or_link_review[1],
  objects_requiring_rebuild = summary$objects_requiring_rebuild[1],
  mean_architecture_readiness_score = summary$mean_architecture_readiness_score[1],
  mean_maintenance_risk_score = summary$mean_maintenance_risk_score[1],
  mean_governance_readiness_score = summary$mean_governance_readiness_score[1],
  governance_controls = summary$governance_controls[1],
  diagnostic_note = "Knowledge architecture review should connect classification, metadata, search, linking, recommendation, provenance, maintenance, representation risk, and editorial governance."
)

write.csv(r_summary, file.path(tables_dir, "r_knowledge_architecture_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
