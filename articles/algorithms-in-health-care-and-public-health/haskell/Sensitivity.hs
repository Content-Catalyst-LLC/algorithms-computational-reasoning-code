module Main where

main :: IO ()
main = do
  let tp = 86.0
      fn = 14.0
      sensitivity = tp / (tp + fn)
  putStrLn ("sensitivity=" ++ show sensitivity)
