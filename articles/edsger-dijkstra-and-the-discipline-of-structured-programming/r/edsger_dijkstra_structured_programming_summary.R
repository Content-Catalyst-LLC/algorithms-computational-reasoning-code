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

map_path <- file.path(tables_dir, "dijkstra_structured_programming_map.csv")
summary_path <- file.path(tables_dir, "dijkstra_structured_programming_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

dijkstra_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "dijkstra_structured_programming_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(dijkstra_map[, c("structured_control", "correctness", "invariants", "proof_relevance", "formal_methods", "readability", "maintainability", "algorithmic_relevance", "system_design", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = dijkstra_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Edsger Dijkstra and the Discipline of Structured Programming")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "dijkstra_discipline_score_by_theme.png"), width = 1000, height = 750)
barplot(dijkstra_map$discipline_score,
        names.arg = dijkstra_map$theme_id,
        las = 2,
        ylab = "Structured Programming Discipline Score",
        main = "Dijkstra Discipline Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_discipline_score = summary$mean_discipline_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Dijkstra should be studied as a theorist of structured programming, correctness, invariants, weakest preconditions, guarded commands, and disciplined software reasoning."
)

write.csv(r_summary, file.path(tables_dir, "r_dijkstra_structured_programming_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
