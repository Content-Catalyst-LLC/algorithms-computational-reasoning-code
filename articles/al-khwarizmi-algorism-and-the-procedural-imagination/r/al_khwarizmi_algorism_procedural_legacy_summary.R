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

map_path <- file.path(tables_dir, "al_khwarizmi_procedural_legacy_map.csv")
summary_path <- file.path(tables_dir, "procedural_legacy_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

legacy_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "procedural_legacy_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(legacy_map[, c("procedure", "representation", "transmission", "application", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = legacy_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Al-Khwārizmī, Algorism, and the Procedural Imagination: Legacy Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "procedural_legacy_score_by_theme.png"), width = 1000, height = 750)
barplot(legacy_map$legacy_score,
        names.arg = legacy_map$theme_id,
        las = 2,
        ylab = "Legacy Score",
        main = "Procedural Legacy Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_legacy_threads = summary$core_legacy_threads[1],
  major_legacy_threads = summary$major_legacy_threads[1],
  supporting_legacy_threads = summary$supporting_legacy_threads[1],
  mean_legacy_score = summary$mean_legacy_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Al-Khwārizmī's legacy should be studied as a procedural, representational, and translational history: central to algorism and algorithmic naming, but not reducible to a single-origin myth."
)

write.csv(r_summary, file.path(tables_dir, "r_procedural_legacy_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
