module PerformanceModels where
data PerformanceMetric = Latency | Throughput | Utilization | TailLatency | ErrorRate | UnitCost deriving (Eq, Show)
