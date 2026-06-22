module Main where

main :: IO ()
main = do
  let scores = [0.62, 0.58, 0.46, 0.52, 0.60, 0.58]
      readiness = sum scores / fromIntegral (length scores)
  putStrLn ("delegation_readiness_score=" ++ show readiness)
