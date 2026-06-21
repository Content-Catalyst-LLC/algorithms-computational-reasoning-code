module Main where

step :: Double -> Double
step x = max 0 (x + 0.08*x - 0.03*x - 0.04*x)

trajectory :: Int -> Double -> [Double]
trajectory 0 x = [x]
trajectory n x = x : trajectory (n - 1) (step x)

main :: IO ()
main = mapM_ print (zip [0 :: Int ..] (trajectory 30 100.0))
