module Distribution where
effectiveCapacity :: Double -> Double -> Double -> Double
effectiveCapacity workers serviceRate overheadRate = max 0 (workers*serviceRate - workers*serviceRate*overheadRate*max (workers-1) 0)
