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

map_path <- file.path(tables_dir, "khwarizmi_algorithmic_method_map.csv")
summary_path <- file.path(tables_dir, "khwarizmi_method_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

method_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "khwarizmi_method_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(method_map[, c("arithmetic_method", "algebraic_procedure", "representation", "transformation", "proof_relation", "transmission", "etymology", "institutional_adoption", "historiographic_caution", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = method_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Al-Khwārizmī and the Historical Roots of Algorithmic Method")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "khwarizmi_method_score_by_theme.png"), width = 1000, height = 750)
barplot(method_map$method_score,
        names.arg = method_map$theme_id,
        las = 2,
        ylab = "Method Score",
        main = "Al-Khwārizmī Method Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_method_score = summary$mean_method_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Al-Khwārizmī should be studied as a decisive bridge in algorithmic method: algorism, algebra, transformation, representation, transmission, and careful historical memory."
)

write.csv(r_summary, file.path(tables_dir, "r_khwarizmi_method_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
