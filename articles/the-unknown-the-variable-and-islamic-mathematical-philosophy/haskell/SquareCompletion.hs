module Main where

main :: IO ()
main = do
  let b = 10.0
      c = 39.0
      completion = (b / 2.0) ** 2
  putStrLn ("completion_term=" ++ show completion)
  putStrLn ("completed_rhs=" ++ show (c + completion))
