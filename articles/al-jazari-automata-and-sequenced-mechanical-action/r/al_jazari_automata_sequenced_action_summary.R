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

map_path <- file.path(tables_dir, "sequenced_action_map.csv")
summary_path <- file.path(tables_dir, "sequenced_action_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

action_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "sequenced_action_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(action_map[, c("sequence_structure", "timing_control", "mechanical_embodiment", "conditional_action", "repeatability", "documentation_quality", "historical_significance", "ethical_caution", "modern_resonance")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = action_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Al-Jazarī Automata and Sequenced Mechanical Action Dimensions")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.70,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "sequenced_action_score_by_theme.png"), width = 1000, height = 750)
barplot(action_map$sequenced_action_score,
        names.arg = action_map$theme_id,
        las = 2,
        ylab = "Sequenced Action Score",
        main = "Sequenced Mechanical Action Score by Theme")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_sequenced_action_score = summary$mean_sequenced_action_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Al-Jazarī’s automata should be studied as sequenced mechanical action: timed state change, conditional triggers, repeatable cycles, mechanical embodiment, and documented reproducibility."
)

write.csv(r_summary, file.path(tables_dir, "r_sequenced_action_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
