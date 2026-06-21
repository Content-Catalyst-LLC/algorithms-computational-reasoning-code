module Main where

f1 :: Double -> Double -> Double
f1 precision recall = if precision + recall == 0 then 0 else 2 * precision * recall / (precision + recall)

main :: IO ()
main = print (f1 0.84 0.76)
