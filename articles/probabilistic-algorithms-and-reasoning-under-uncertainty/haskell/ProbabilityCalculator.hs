module Main where

standardError :: Double -> Double -> Double
standardError pHat n = sqrt ((pHat * (1 - pHat)) / n)

main :: IO ()
main = putStrLn $ "p_hat=0.57 standard_error=" ++ show (standardError 0.57 1000)
