WITH RECURSIVE sum_loop(i, acc) AS (
  VALUES (0, 0)
  UNION ALL
  SELECT i + 1, acc + i
  FROM sum_loop
  WHERE i <= 5
)
SELECT MAX(acc) AS sum_to_5
FROM sum_loop;
