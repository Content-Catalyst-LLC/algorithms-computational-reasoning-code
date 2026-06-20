module Main where

weights :: [Double]
weights = [0.10,0.11,0.11,0.09,0.09,0.10,0.09,0.09,0.08,0.06,0.06,0.02]

identityAccessScore :: [Double] -> Double
identityAccessScore xs = 100 * sum (zipWith (*) xs weights)

main :: IO ()
main = print (identityAccessScore (replicate 12 0.75))
