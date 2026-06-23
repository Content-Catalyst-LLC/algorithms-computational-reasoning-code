module Main where

main :: IO ()
main = mapM_ showGrowth [10.0, 100.0, 1000.0, 10000.0]
  where
    showGrowth n = putStrLn ("n=" ++ show n ++ ", log2=" ++ show (logBase 2 n) ++ ", nlogn=" ++ show (n * logBase 2 n) ++ ", n2=" ++ show (n*n))
