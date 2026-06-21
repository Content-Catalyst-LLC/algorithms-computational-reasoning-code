module Main where

f :: Double -> Double
f x = sin x + 0.25 * x * x

centralDifference :: Double -> Double -> Double
centralDifference x h = (f (x + h) - f (x - h)) / (2 * h)

main :: IO ()
main = print (centralDifference 1.0 0.01)
