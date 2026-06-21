module Main where

f :: Double -> Double
f = sin

centralDifference :: Double -> Double -> Double
centralDifference x h = (f (x + h) - f (x - h)) / (2 * h)

trapezoid :: Int -> Double
trapezoid n = h * (0.5 * f a + sum [f (a + fromIntegral i * h) | i <- [1..n-1]] + 0.5 * f b)
  where
    a = 0.0
    b = pi
    h = (b - a) / fromIntegral n

main :: IO ()
main = do
  putStrLn $ "central difference: " ++ show (centralDifference 1.0 1e-4)
  putStrLn $ "trapezoid integral: " ++ show (trapezoid 200)
