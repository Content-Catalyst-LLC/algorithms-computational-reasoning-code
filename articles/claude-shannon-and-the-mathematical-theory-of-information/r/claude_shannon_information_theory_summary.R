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

map_path <- file.path(tables_dir, "shannon_information_map.csv")
summary_path <- file.path(tables_dir, "shannon_information_summary.csv")

if (!file.exists(map_path)) {
  stop(paste("Missing", map_path, "Run the Python workflow first."))
}

shannon_map <- read.csv(map_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "shannon_information_dimensions.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(shannon_map[, c("entropy_centrality", "coding_relevance", "channel_capacity", "noise_awareness", "redundancy_design", "computation_relevance", "cryptography_relevance", "ai_relevance", "semantic_boundary", "governance_caution")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = shannon_map$theme_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Interpretive Score",
        main = "Claude Shannon and the Mathematical Theory of Information")
legend("bottomright",
       legend = rownames(score_matrix),
       cex = 0.68,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "shannon_information_score_by_theme.png"), width = 1000, height = 750)
barplot(shannon_map$information_score,
        names.arg = shannon_map$theme_id,
        las = 2,
        ylab = "Information Theory Score",
        main = "Shannon Information Theory Score by Theme")
grid()
dev.off()

entropy_examples <- read.csv(file.path(tables_dir, "entropy_examples.csv"), stringsAsFactors = FALSE)

png(file.path(figures_dir, "entropy_examples.png"), width = 900, height = 650)
barplot(entropy_examples$entropy_bits,
        names.arg = entropy_examples$source,
        las = 2,
        ylab = "Entropy in bits",
        main = "Entropy Examples")
grid()
dev.off()

r_summary <- data.frame(
  themes_reviewed = summary$themes_reviewed[1],
  core_threads = summary$core_threads[1],
  major_threads = summary$major_threads[1],
  supporting_threads = summary$supporting_threads[1],
  mean_information_score = summary$mean_information_score[1],
  cautions = summary$cautions[1],
  diagnostic_note = "Shannon should be studied as the architect of mathematical information theory: entropy, coding, capacity, noise, redundancy, reliability, and semantic boundaries."
)

write.csv(r_summary, file.path(tables_dir, "r_shannon_information_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
