WITH probabilities(symbol, p) AS (
  VALUES ('0', 0.5), ('1', 0.5)
)
SELECT
  -SUM(p * (LN(p) / LN(2.0))) AS entropy_bits
FROM probabilities
WHERE p > 0;
