module Main where

sumTo :: Int -> Int
sumTo n = loop 0 0
  where
    loop i acc
      | i > n = acc
      | otherwise = loop (i + 1) (acc + i)

main :: IO ()
main = print (sumTo 5)
