# Self-contained R hash-verification calculator using base R.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

out_dir <- file.path(article_root, "calculators", "outputs")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

# Lightweight base-R teaching checksum, not cryptographic.
teaching_checksum <- function(text) {
  ints <- utf8ToInt(text)
  sum(ints * seq_along(ints)) %% 1000003
}

texts <- c("verified artifact manifest", "verified artifact manifest!")
result <- data.frame(
  case = c("original", "altered"),
  teaching_checksum = sapply(texts, teaching_checksum),
  text_length = nchar(texts),
  stringsAsFactors = FALSE
)
result$matches_original_checksum <- result$teaching_checksum == result$teaching_checksum[1]

out_path <- file.path(out_dir, "r_hash_verification_calculator.csv")
write.csv(result, out_path, row.names = FALSE)
print(out_path)
