module Main where

main :: IO ()
main = do
  let scores = [0.60, 0.62, 0.58, 0.52, 0.46, 0.50]
      readiness = sum scores / fromIntegral (length scores)
  putStrLn ("governance_readiness_score=" ++ show readiness)
