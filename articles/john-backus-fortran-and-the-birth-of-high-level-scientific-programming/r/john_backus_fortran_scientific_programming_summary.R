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

map_path <- file.path(tables_dir, "backus_fortran_scientific_programming_map.csv")
summary_path <- file.path(tables_dir, "backus_fortran_scientific_programming_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

backus_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "backus_fortran_scientific_programming_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(backus_map[, c("high_level_language", "scientific_expression", "compiler_optimization", "numerical_relevance", "portability", "performance_credibility", "language_history", "formal_specification", "maintainability", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = backus_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "John Backus, Fortran, and the Birth of High-Level Scientific Programming")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "backus_birth_score_by_theme.png"), width = 1000, height = 750)
barplot(backus_map$birth_score,
        names.arg = backus_map$theme_id,
        las = 2,
        ylab = "High-Level Scientific Programming Birth Score",
        main = "Backus/Fortran Score by Theme")
grid()
dev.off()

if (file.exists(file.path(tables_dir, "formula_translation_example.csv"))) {
  formula <- read.csv(file.path(tables_dir, "formula_translation_example.csv"))
  png(file.path(figures_dir, "formula_translation_example.png"), width = 950, height = 700)
  plot(formula$x, formula$y,
       type = "b",
       xlab = "x",
       ylab = "y = 2x^2 - 3x + 1",
       main = "Formula Translation Example")
  grid()
  dev.off()
}

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_birth_score = summary$mean_birth_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Backus and FORTRAN should be studied as the practical birth of high-level scientific programming: formula translation, compiler optimization, numerical expression, and performance-oriented abstraction."
)

write.csv(r_summary, file.path(tables_dir, "r_backus_fortran_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
