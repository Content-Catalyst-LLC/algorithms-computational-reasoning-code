args <- commandArgs(trailingOnly = TRUE)
expected <- ifelse(length(args) >= 1, args[1], "source:a;source:b")
found <- ifelse(length(args) >= 2, args[2], "source:a")
parse_sources <- function(x) {
  if (nchar(x) == 0) return(character())
  trimws(gsub("source:", "", unlist(strsplit(x, ";"))))
}
expected_set <- parse_sources(expected)
found_set <- parse_sources(found)
missing <- setdiff(expected_set, found_set)
score <- ifelse(length(expected_set) > 0 && length(missing) == 0, 1, 0)
cat(sprintf("source_score=%.6f\n", score))
cat(sprintf("missing=%s\n", paste(missing, collapse = ";")))
