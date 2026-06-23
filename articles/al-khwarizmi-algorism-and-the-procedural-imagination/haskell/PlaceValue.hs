module Main where

main :: IO ()
main = do
  let digit = 7
      base = 10
      position = 3
      value = digit * (base ^ position)
  putStrLn ("place_value=" ++ show value)
