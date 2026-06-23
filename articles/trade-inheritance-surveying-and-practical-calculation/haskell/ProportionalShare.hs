module Main where

main :: IO ()
main = do
  let total = 1200.0
      weights = [2.0, 1.0, 1.0]
      shares = map (\w -> total * w / sum weights) weights
  print shares
