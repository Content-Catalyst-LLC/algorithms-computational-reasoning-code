module ParallelComputation where
data ParallelPattern = DataParallel | TaskParallel | PipelineParallel | MapReduce | Vectorized | GPUParallel deriving (Eq, Show)
