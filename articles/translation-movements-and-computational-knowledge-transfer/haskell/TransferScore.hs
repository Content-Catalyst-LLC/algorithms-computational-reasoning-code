module Main where

main :: IO ()
main = do
  let scores = [0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96]
      score = sum scores / fromIntegral (length scores)
  putStrLn ("transfer_score=" ++ show score)
