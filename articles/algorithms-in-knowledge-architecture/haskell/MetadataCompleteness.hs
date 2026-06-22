module Main where

main :: IO ()
main = do
  let presentFields = 11.0
      requiredFields = 12.0
      score = presentFields / requiredFields
  putStrLn ("metadata_completeness_score=" ++ show score)
