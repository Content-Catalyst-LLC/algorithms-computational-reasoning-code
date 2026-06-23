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

map_path <- file.path(tables_dir, "positional_calculation_transmission_map.csv")
summary_path <- file.path(tables_dir, "positional_calculation_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

position_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "positional_calculation_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(position_map[, c("representation", "procedure", "transmission", "practical_use", "pedagogy", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = position_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Hindu-Arabic Numerals: Positional Calculation Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "positional_score_by_theme.png"), width = 1000, height = 750)
barplot(position_map$positional_score,
        names.arg = position_map$theme_id,
        las = 2,
        ylab = "Positional Calculation Score",
        main = "Positional Calculation Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_positional_score = summary$mean_positional_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Hindu-Arabic numerals should be studied as representational, procedural, pedagogical, practical, and translational infrastructure for algorithmic reasoning."
)

write.csv(r_summary, file.path(tables_dir, "r_positional_calculation_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
