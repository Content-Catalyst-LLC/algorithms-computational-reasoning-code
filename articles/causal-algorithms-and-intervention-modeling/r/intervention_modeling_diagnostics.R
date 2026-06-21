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
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)
estimates_path <- file.path(tables_dir, "intervention_effect_estimates.csv")
if (!file.exists(estimates_path)) stop("Run the Python workflow first.")
estimates <- read.csv(estimates_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "intervention_mean_effects.png"), width = 1300, height = 850)
barplot(estimates$mean_estimated_effect, names.arg = estimates$intervention_name, las = 2, ylab = "Mean estimated effect", main = "Modeled Intervention Effects")
grid()
dev.off()
png(file.path(figures_dir, "intervention_net_benefit.png"), width = 1300, height = 850)
barplot(estimates$mean_net_benefit, names.arg = estimates$intervention_name, las = 2, ylab = "Mean net benefit", main = "Modeled Net Benefit by Intervention")
abline(h = 0, lty = 2)
grid()
dev.off()
summary_table <- data.frame(
  interventions = nrow(estimates),
  best_effect = estimates$intervention_name[which.max(estimates$mean_estimated_effect)],
  best_net_benefit = estimates$intervention_name[which.max(estimates$mean_net_benefit)]
)
write.csv(summary_table, file.path(tables_dir, "r_intervention_modeling_summary.csv"), row.names = FALSE)
print(summary_table)
