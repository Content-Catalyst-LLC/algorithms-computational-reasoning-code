module VectorTypes where

type Vector = [Double]
dot :: Vector -> Vector -> Double
dot xs ys = sum (zipWith (*) xs ys)

magnitude :: Vector -> Double
magnitude xs = sqrt (sum (map (^2) xs))
