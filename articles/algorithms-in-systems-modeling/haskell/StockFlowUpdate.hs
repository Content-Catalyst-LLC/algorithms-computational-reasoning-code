module Main where

main :: IO ()
main = do
  let currentStock = 100.0
      inflow = 12.0
      outflow = 7.0
      nextStock = currentStock + inflow - outflow
  putStrLn ("next_stock=" ++ show nextStock)
