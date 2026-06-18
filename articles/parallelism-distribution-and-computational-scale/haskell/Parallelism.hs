module Parallelism where
data ParallelismType = Task | DataParallel | Pipeline | Model deriving (Eq, Show)
