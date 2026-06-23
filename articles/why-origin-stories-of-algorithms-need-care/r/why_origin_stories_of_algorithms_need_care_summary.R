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

map_path <- file.path(tables_dir, "origin_story_care_map.csv")
summary_path <- file.path(tables_dir, "origin_story_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

origin_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "origin_story_care_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(origin_map[, c("evidence_grounding", "scope_clarity", "anachronism_control", "network_awareness", "etymology_caution", "transmission_depth", "credit_distribution", "public_usefulness", "historical_significance", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = origin_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Why Origin Stories of Algorithms Need Care: Historiography Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "origin_care_score_by_theme.png"), width = 1000, height = 750)
barplot(origin_map$origin_care_score,
        names.arg = origin_map$theme_id,
        las = 2,
        ylab = "Origin-Care Score",
        main = "Algorithm Origin-Story Care Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_origin_care_score = summary$mean_origin_care_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Algorithm origin stories need care because word histories, concept histories, procedure histories, transmission histories, and modern formalization do not all begin at the same point."
)

write.csv(r_summary, file.path(tables_dir, "r_origin_story_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
