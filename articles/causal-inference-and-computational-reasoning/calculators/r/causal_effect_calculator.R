args <- commandArgs(trailingOnly = TRUE)
values <- list()
for (arg in args) {
  parts <- strsplit(sub("^--", "", arg), "=", fixed = TRUE)[[1]]
  if (length(parts) == 2) values[[parts[1]]] <- as.numeric(parts[2])
}
if (is.null(values[["treated-mean"]]) || is.null(values[["control-mean"]])) {
  stop("Usage: Rscript causal_effect_calculator.R --treated-mean=0.62 --control-mean=0.41")
}
effect <- values[["treated-mean"]] - values[["control-mean"]]
cat(sprintf("treated_mean=%.6f\n", values[["treated-mean"]]))
cat(sprintf("control_mean=%.6f\n", values[["control-mean"]]))
cat(sprintf("difference=%.6f\n", effect))
