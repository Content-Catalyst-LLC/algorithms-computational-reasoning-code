module ConcurrencyModels where
data ConcurrencyModel = Threads | Processes | AsyncTasks | Actors | MessageQueues | DistributedWorkers deriving (Eq, Show)
