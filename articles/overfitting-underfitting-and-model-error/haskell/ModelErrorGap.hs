module Main where
gap :: Double -> Double -> Double
gap train test = test - train
main :: IO ()
main = print (gap 0.04 0.09)
