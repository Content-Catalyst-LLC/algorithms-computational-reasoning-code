module Main where

main :: IO ()
main = do
  let b = 6.0
      term = (b / 2.0) ** 2
  putStrLn ("completing_term=" ++ show term)
