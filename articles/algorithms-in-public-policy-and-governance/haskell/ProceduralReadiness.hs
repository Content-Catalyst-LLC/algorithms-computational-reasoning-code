module Main where

main :: IO ()
main = do
  let dueProcess = 0.58
      transparency = 0.52
      humanReview = 0.60
      appealReadiness = 0.54
      score = (dueProcess + transparency + humanReview + appealReadiness) / 4.0
  putStrLn ("procedural_readiness_score=" ++ show score)
