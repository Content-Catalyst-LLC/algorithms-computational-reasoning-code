args <- commandArgs(trailingOnly = TRUE)
agents <- ifelse(length(args) >= 1, as.integer(args[1]), 100)
threshold <- ifelse(length(args) >= 2, as.numeric(args[2]), 0.5)
steps <- ifelse(length(args) >= 3, as.integer(args[3]), 30)
seed <- ifelse(length(args) >= 4, as.integer(args[4]), 7)

set.seed(seed)
adopted <- runif(agents) < 0.08
rows <- data.frame()
for (step in 0:steps) {
  share <- sum(adopted) / agents
  rows <- rbind(rows, data.frame(step = step, agents = agents, threshold = threshold, adoption_share = round(share, 6), seed = seed))
  if (step == steps) break
  next_adopted <- adopted
  for (i in seq_len(agents)) {
    if (adopted[i]) next
    left <- adopted[ifelse(i == 1, agents, i - 1)]
    right <- adopted[ifelse(i == agents, 1, i + 1)]
    local_share <- (as.integer(left) + as.integer(right)) / 2
    if (local_share >= threshold || runif(1) < 0.015) next_adopted[i] <- TRUE
  }
  adopted <- next_adopted
}

article_root <- normalizePath(file.path(dirname(sys.frame(1)$ofile %||% getwd()), "../.."), mustWork = FALSE)
if (!dir.exists(file.path(article_root, "outputs", "tables"))) {
  article_root <- getwd()
}
out_dir <- file.path(article_root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
out_path <- file.path(out_dir, "r_agent_based_calculator_output.csv")
write.csv(rows, out_path, row.names = FALSE)
print(out_path)
