module Main where

main :: IO ()
main = do
  let n = 1000.0
  putStrLn ("log2_n=" ++ show (logBase 2 n))
  putStrLn ("n=" ++ show n)
  putStrLn ("n_log2_n=" ++ show (n * logBase 2 n))
  putStrLn ("n_squared=" ++ show (n * n))
