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

map_path <- file.path(tables_dir, "practical_calculation_procedure_map.csv")
summary_path <- file.path(tables_dir, "practical_calculation_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

practical_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "practical_calculation_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(practical_map[, c("procedure", "representation", "institutional_importance", "verification", "transmission", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = practical_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Trade, Inheritance, Surveying, and Practical Calculation Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "practical_score_by_theme.png"), width = 1000, height = 750)
barplot(practical_map$practical_score,
        names.arg = practical_map$theme_id,
        las = 2,
        ylab = "Practical Calculation Score",
        main = "Practical Calculation Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_practical_score = summary$mean_practical_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Practical calculation should be studied as institutional algorithmic reasoning: rule-governed methods for allocation, measurement, trade, recordkeeping, verification, and trust."
)

write.csv(r_summary, file.path(tables_dir, "r_practical_calculation_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
