module DatabaseOptimization where
data OptimizationMove = Pushdown | ProjectionPruning | Indexing | Materialization | StatisticsRefresh deriving (Eq, Show)
