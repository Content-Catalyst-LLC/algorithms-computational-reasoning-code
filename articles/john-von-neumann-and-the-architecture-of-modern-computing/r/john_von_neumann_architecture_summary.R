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

map_path <- file.path(tables_dir, "von_neumann_architecture_map.csv")
summary_path <- file.path(tables_dir, "von_neumann_architecture_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

architecture_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "von_neumann_architecture_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(architecture_map[, c("stored_program", "memory_organization", "control_structure", "program_as_data", "implementation_influence", "bottleneck_awareness", "collaboration_context", "software_relevance", "ai_infrastructure", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = architecture_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "John von Neumann and the Architecture of Modern Computing")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "von_neumann_architecture_score_by_theme.png"), width = 1000, height = 750)
barplot(architecture_map$architecture_score,
        names.arg = architecture_map$theme_id,
        las = 2,
        ylab = "Architecture Score",
        main = "von Neumann Architecture Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_architecture_score = summary$mean_architecture_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "von Neumann should be studied as an architectural synthesizer of stored-program computing, shared memory, control, software layers, bottlenecks, and institutional computing."
)

write.csv(r_summary, file.path(tables_dir, "r_von_neumann_architecture_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
