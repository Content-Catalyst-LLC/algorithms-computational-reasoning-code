args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 3) {
  stop("Usage: Rscript counterfactual_calculator.R <original_score> <counterfactual_score> <threshold>")
}
original <- as.numeric(args[1])
counterfactual <- as.numeric(args[2])
threshold <- as.numeric(args[3])
original_label <- ifelse(original >= threshold, "favorable", "not_favorable")
counterfactual_label <- ifelse(counterfactual >= threshold, "favorable", "not_favorable")
cat(sprintf("original_label=%s\n", original_label))
cat(sprintf("counterfactual_label=%s\n", counterfactual_label))
cat(sprintf("score_change=%.6f\n", counterfactual - original))
cat(sprintf("decision_flipped=%s\n", original_label != counterfactual_label))
