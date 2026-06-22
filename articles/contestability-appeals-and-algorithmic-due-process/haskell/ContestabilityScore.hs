module Main where

main :: IO ()
main = do
  let notice = 0.70
      reasons = 0.62
      evidenceAccess = 0.48
      humanReview = 0.55
      correction = 0.52
      remedy = 0.44
      score = (notice + reasons + evidenceAccess + humanReview + correction + remedy) / 6
  putStrLn ("contestability_score=" ++ show score)
