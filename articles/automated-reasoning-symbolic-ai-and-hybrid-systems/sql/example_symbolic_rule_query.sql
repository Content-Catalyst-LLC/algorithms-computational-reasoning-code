WITH facts(fact) AS (
  VALUES ('has_documentation'), ('logs_decisions')
),
premises(premise) AS (
  VALUES ('has_documentation'), ('logs_decisions')
)
SELECT
  CASE
    WHEN (SELECT COUNT(*) FROM premises WHERE premise NOT IN (SELECT fact FROM facts)) = 0
    THEN 'traceable_system'
    ELSE 'not_derived'
  END AS conclusion;
