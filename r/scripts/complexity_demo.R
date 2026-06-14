# Algorithms & Computational Reasoning: minimal R complexity demo

dir.create("outputs", showWarnings = FALSE, recursive = TRUE)

n <- c(1, 10, 100, 1000)
df <- data.frame(
  n = n,
  linear = n,
  quadratic = n^2,
  cubic = n^3
)

write.csv(df, "outputs/r_complexity_demo.csv", row.names = FALSE)
print(df)
