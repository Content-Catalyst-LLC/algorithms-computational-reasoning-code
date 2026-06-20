# Base R secure-communication governance calculator.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

output_dir <- file.path(article_root, "calculators", "outputs")
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE)
}

score_case <- function(threat_model, protocols, keys, validation, integrity, authentication, randomness, secret_storage, rotation, implementation_review) {
  100 * (
    0.12 * threat_model +
      0.10 * protocols +
      0.14 * keys +
      0.10 * validation +
      0.10 * integrity +
      0.10 * authentication +
      0.08 * randomness +
      0.10 * secret_storage +
      0.08 * rotation +
      0.08 * implementation_review
  )
}

rows <- data.frame(
  case = c("standard secure channel", "legacy manual transfer"),
  score = c(
    score_case(0.86, 0.88, 0.82, 0.90, 0.86, 0.84, 0.84, 0.82, 0.78, 0.80),
    score_case(0.36, 0.28, 0.24, 0.18, 0.34, 0.28, 0.30, 0.22, 0.16, 0.20)
  )
)

write.csv(rows, file.path(output_dir, "r_secure_communication_calculator.csv"), row.names = FALSE)
print(rows)
