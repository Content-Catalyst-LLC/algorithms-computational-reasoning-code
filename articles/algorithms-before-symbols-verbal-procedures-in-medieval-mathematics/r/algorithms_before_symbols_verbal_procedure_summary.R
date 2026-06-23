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

map_path <- file.path(tables_dir, "verbal_procedure_map.csv")
summary_path <- file.path(tables_dir, "verbal_procedure_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

verbal_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "verbal_procedure_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(verbal_map[, c("procedural_clarity", "representation_dependence", "pedagogical_value", "transmission_importance", "practical_use", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = verbal_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Algorithms Before Symbols: Verbal Procedure Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "verbal_procedure_score_by_theme.png"), width = 1000, height = 750)
barplot(verbal_map$verbal_procedure_score,
        names.arg = verbal_map$theme_id,
        las = 2,
        ylab = "Verbal Procedure Score",
        main = "Verbal Procedure Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_verbal_procedure_score = summary$mean_verbal_procedure_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Algorithms before symbols should be studied as verbal, pedagogical, representational, practical, and transmissible procedures rather than as modern code projected backward."
)

write.csv(r_summary, file.path(tables_dir, "r_verbal_procedure_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
