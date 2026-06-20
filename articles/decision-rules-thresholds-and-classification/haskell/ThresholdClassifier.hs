module Main where

classify :: Double -> Double -> Int
classify score threshold = if score >= threshold then 1 else 0

main :: IO ()
main = print (classify 0.72 0.50)
