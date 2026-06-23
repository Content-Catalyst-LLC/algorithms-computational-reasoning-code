module Main where

-- Lightweight placeholder example: a real Bernoulli implementation would use rationals carefully.
operationSequence :: [String]
operationSequence = ["initialize", "store", "multiply", "subtract", "repeat", "output"]

main :: IO ()
main = putStrLn ("operation_sequence=" ++ unwords operationSequence)
