module Main where

main :: IO ()
main = do
  let level = 7.5
      threshold = 5.0
      actionTriggered = level >= threshold
  putStrLn ("action_triggered=" ++ show actionTriggered)
