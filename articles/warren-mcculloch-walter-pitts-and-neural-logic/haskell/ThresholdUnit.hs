module Main where

thresholdUnit :: [Int] -> [Int] -> Int -> Int
thresholdUnit inputs weights threshold =
  if sum (zipWith (*) inputs weights) >= threshold then 1 else 0

main :: IO ()
main = print (thresholdUnit [1, 1] [1, 1] 2)
