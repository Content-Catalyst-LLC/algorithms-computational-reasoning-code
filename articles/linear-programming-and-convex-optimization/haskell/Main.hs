module Main where

objective :: Int -> Int -> Int
objective x y = 3*x + 4*y

feasible :: Int -> Int -> Bool
feasible x y = 2*x + y <= 8 && x + 2*y <= 8 && x >= 0 && y >= 0

main :: IO ()
main = do
  let candidates = [(x, y, objective x y) | x <- [0..9], y <- [0..9], feasible x y]
  print (maximum [(value, x, y) | (x, y, value) <- candidates])
