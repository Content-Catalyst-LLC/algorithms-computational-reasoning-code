module Main where

main :: IO ()
main = do
  let scores = [0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98]
      score = sum scores / fromIntegral (length scores)
  putStrLn ("origin_care_score=" ++ show score)
