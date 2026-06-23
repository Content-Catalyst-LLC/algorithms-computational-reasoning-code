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

map_path <- file.path(tables_dir, "historical_algorithmic_reasoning_map.csv")
summary_path <- file.path(tables_dir, "historical_reasoning_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

theme_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "historical_theme_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(theme_map[, c("procedural_explicitness", "transmission_importance", "practical_application", "representation_importance", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = theme_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Islamic-World Roots of Algorithmic Reasoning: Historical Theme Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "historical_significance_by_theme.png"), width = 1000, height = 750)
barplot(theme_map$significance_score,
        names.arg = theme_map$theme_id,
        las = 2,
        ylab = "Significance Score",
        main = "Historical Algorithmic-Reasoning Significance by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_significance_score = summary$mean_significance_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Islamic-world roots of algorithmic reasoning should be studied as procedural, translational, practical, representational, and institutional history without reducing algorithms to a single-origin story."
)

write.csv(r_summary, file.path(tables_dir, "r_historical_theme_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
