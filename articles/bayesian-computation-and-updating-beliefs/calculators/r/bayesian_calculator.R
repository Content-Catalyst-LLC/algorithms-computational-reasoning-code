args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag, default) { hit <- grep(paste0("^", flag, "="), args, value = TRUE); if (length(hit) == 0) return(default); sub(paste0("^", flag, "="), "", hit[1]) }
alpha <- as.numeric(get_arg("--alpha", "2")); beta <- as.numeric(get_arg("--beta", "2")); successes <- as.integer(get_arg("--successes", "113")); failures <- as.integer(get_arg("--failures", "72")); threshold <- as.numeric(get_arg("--threshold", "0.60"))
post_alpha <- alpha + successes; post_beta <- beta + failures; posterior_mean <- post_alpha / (post_alpha + post_beta); posterior_variance <- (post_alpha * post_beta) / (((post_alpha + post_beta)^2) * (post_alpha + post_beta + 1))
output <- data.frame(prior_alpha = alpha, prior_beta = beta, successes = successes, failures = failures, posterior_alpha = post_alpha, posterior_beta = post_beta, posterior_mean = posterior_mean, posterior_sd = sqrt(posterior_variance), credible_interval_90_lower = qbeta(0.05, post_alpha, post_beta), credible_interval_90_upper = qbeta(0.95, post_alpha, post_beta), threshold = threshold, probability_above_threshold = 1 - pbeta(threshold, post_alpha, post_beta))
script_args <- commandArgs(trailingOnly = FALSE); file_arg <- grep("^--file=", script_args, value = TRUE)
if (length(file_arg) > 0) { script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE); out_dir <- file.path(dirname(dirname(script_path)), "outputs") } else { out_dir <- file.path(getwd(), "calculators", "outputs") }
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(output, file.path(out_dir, "bayesian_calculator_output_r.csv"), row.names = FALSE)
print(output)
