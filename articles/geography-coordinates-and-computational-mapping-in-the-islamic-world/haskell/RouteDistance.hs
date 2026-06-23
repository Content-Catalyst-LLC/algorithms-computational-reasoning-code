module Main where

main :: IO ()
main = do
  let segments = [12.0, 20.0, 7.5]
  putStrLn ("segments=" ++ show (length segments))
  putStrLn ("total_distance=" ++ show (sum segments))
