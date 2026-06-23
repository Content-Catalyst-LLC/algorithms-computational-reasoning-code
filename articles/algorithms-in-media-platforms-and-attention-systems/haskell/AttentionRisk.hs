module Main where

main :: IO ()
main = do
  let engagementPressure = 0.92
      creatorImpact = 0.88
      publicKnowledgeImpact = 0.78
      userControl = 0.44
      contestability = 0.42
      score = (engagementPressure + creatorImpact + publicKnowledgeImpact + (1 - userControl) + (1 - contestability)) / 5.0
  putStrLn ("attention_risk_score=" ++ show score)
