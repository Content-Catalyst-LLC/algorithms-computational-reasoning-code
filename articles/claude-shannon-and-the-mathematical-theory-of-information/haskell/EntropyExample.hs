module Main where

entropy :: [Double] -> Double
entropy ps = negate (sum [p * logBase 2 p | p <- ps, p > 0])

main :: IO ()
main = putStrLn ("entropy_bits=" ++ show (entropy [0.5, 0.5]))
