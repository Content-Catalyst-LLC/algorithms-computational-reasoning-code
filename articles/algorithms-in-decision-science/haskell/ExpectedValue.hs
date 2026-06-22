module Main where

main :: IO ()
main = do
  let probability = 0.82
      benefitIfAct = 0.88
      costIfAct = 0.30
      expectedValue = probability * benefitIfAct - costIfAct
  putStrLn ("expected_value_of_action=" ++ show expectedValue)
