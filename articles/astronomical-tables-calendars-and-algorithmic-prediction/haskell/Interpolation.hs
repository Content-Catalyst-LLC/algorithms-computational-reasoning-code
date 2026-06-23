module Main where

main :: IO ()
main = do
  let x0 = 10.0
      y0 = 1.2
      x1 = 20.0
      y1 = 2.8
      x = 15.0
      y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0)
  putStrLn ("interpolated_y=" ++ show y)
