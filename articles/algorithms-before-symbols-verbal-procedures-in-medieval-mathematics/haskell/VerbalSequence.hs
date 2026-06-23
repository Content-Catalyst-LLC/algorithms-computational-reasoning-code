module Main where

main :: IO ()
main = mapM_ putStrLn
  [ "1: take the number"
  , "2: double it"
  , "3: add the adjustment"
  , "4: check the result"
  ]
