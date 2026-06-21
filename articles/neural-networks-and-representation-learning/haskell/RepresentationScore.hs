module Main where

sigmoid :: Double -> Double
sigmoid x = 1 / (1 + exp (-x))

representationScore :: Double -> Double -> Double -> Double -> Double
representationScore x1 x2 x3 bias = sigmoid (0.9*x1 - 0.7*x2 + 0.35*x3 + bias)

main :: IO ()
main = print (representationScore 0.5 (-0.2) 0.7 0.0)
