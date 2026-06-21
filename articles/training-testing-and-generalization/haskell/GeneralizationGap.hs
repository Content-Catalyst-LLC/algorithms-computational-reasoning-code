module Main where
gap :: Double -> Double -> Double
gap train test = train - test
main :: IO ()
main = print (gap 0.88 0.81)
