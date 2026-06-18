module FaultTolerance where
data FailureModel = Crash | Omission | Timing | Partition | Restart | Byzantine | Operator | Dependency deriving (Eq, Show)
