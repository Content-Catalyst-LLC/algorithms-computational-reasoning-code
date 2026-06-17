module FunctionalStyle where

average :: [Double] -> Double
average [] = 0
average xs = sum xs / fromIntegral (length xs)

composeExample :: (b -> c) -> (a -> b) -> a -> c
composeExample g f x = g (f x)
