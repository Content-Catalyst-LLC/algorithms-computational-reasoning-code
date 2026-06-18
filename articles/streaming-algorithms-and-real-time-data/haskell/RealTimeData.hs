module RealTimeData where
stableQueue :: Double -> Double -> Bool
stableQueue arrival processing = arrival < processing
