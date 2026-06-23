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

map_path <- file.path(tables_dir, "knuth_algorithmic_art_map.csv")
summary_path <- file.path(tables_dir, "knuth_algorithmic_art_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

knuth_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "knuth_algorithmic_art_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(knuth_map[, c("algorithm_analysis", "exposition", "mathematical_rigor", "historical_depth", "implementation_relevance", "typography_relevance", "literate_programming", "pedagogy", "maintainability", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = knuth_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Donald Knuth and the Art of Computer Programming")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "knuth_art_score_by_theme.png"), width = 1000, height = 750)
barplot(knuth_map$art_score,
        names.arg = knuth_map$theme_id,
        las = 2,
        ylab = "Algorithmic Art Score",
        main = "Knuth Algorithmic Art Score by Theme")
grid()
dev.off()

if (file.exists(file.path(tables_dir, "growth_table.csv"))) {
  growth <- read.csv(file.path(tables_dir, "growth_table.csv"))
  png(file.path(figures_dir, "knuth_growth_comparison.png"), width = 950, height = 700)
  matplot(growth$n, cbind(growth$log2_n, growth$n, growth$n_log2_n),
          type = "b", log = "xy", lty = 1, pch = 1,
          xlab = "n", ylab = "cost on log-log scale",
          main = "Growth Comparison")
  legend("topleft", legend = c("log2 n", "n", "n log2 n"), lty = 1, pch = 1, bty = "n")
  grid()
  dev.off()
}

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_art_score = summary$mean_art_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Knuth should be studied as a theorist of algorithmic analysis, rigorous exposition, literate programming, typography, and computational craft."
)

write.csv(r_summary, file.path(tables_dir, "r_knuth_algorithmic_art_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
