module Main where

gcdAlgorithm :: Int -> Int -> Int
gcdAlgorithm a 0 = abs a
gcdAlgorithm a b = gcdAlgorithm b (a `mod` b)

main :: IO ()
main = putStrLn ("gcd=" ++ show (gcdAlgorithm 252 105))
