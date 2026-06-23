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

map_path <- file.path(tables_dir, "astronomical_prediction_map.csv")
summary_path <- file.path(tables_dir, "astronomical_prediction_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

prediction_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "astronomical_prediction_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(prediction_map[, c("table_structure", "procedural_clarity", "predictive_function", "institutional_use", "correction_awareness", "transmission_importance", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = prediction_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Astronomical Tables, Calendars, and Algorithmic Prediction Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "prediction_score_by_theme.png"), width = 1000, height = 750)
barplot(prediction_map$prediction_score,
        names.arg = prediction_map$theme_id,
        las = 2,
        ylab = "Prediction Score",
        main = "Astronomical Prediction Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_prediction_score = summary$mean_prediction_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Astronomical tables and calendars should be studied as algorithmic prediction systems: stored computation, procedural lookup, correction, interpolation, calendar rules, and institutional timekeeping."
)

write.csv(r_summary, file.path(tables_dir, "r_astronomical_prediction_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
