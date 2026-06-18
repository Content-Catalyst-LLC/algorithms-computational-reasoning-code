module PracticalSolvability where
relativeGap :: Double -> Double -> Double
relativeGap alg bound = (alg - bound) / bound
