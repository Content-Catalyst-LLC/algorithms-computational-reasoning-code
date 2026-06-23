module Main where

main :: IO ()
main = do
  let value = 12.0
      trigger = 10.0
      eventTriggered = value >= trigger
  putStrLn ("event_triggered=" ++ show eventTriggered)
