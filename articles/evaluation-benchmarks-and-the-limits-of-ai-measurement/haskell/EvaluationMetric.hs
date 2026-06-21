module Main where

safeDiv :: Double -> Double -> Double
safeDiv _ 0 = 0
safeDiv x y = x / y

main :: IO ()
main = do
  let tp = 42
      tn = 38
      fp = 7
      fn = 13
      accuracy = safeDiv (tp + tn) (tp + tn + fp + fn)
  putStrLn ("accuracy=" ++ show accuracy)
