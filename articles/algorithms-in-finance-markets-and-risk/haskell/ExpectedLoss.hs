module Main where

main :: IO ()
main = do
  let pd = 0.035
      lgd = 0.45
      ead = 100000.0
      expectedLoss = pd * lgd * ead
  putStrLn ("expected_loss=" ++ show expectedLoss)
