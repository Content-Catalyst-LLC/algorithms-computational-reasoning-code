module DistributedModels where
data FailureModel = Crash | Delay | Partition | Overload | Byzantine deriving (Eq, Show)
data ConsistencyModel = Strong | Eventual | Causal | Snapshot | Linearizable deriving (Eq, Show)
