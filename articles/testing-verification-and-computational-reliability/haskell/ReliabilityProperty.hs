module ReliabilityProperty where
scoreInRange :: Double -> Bool
scoreInRange x = x >= 0 && x <= 100
