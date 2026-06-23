module Main where

churchApply :: Int -> (a -> a) -> a -> a
churchApply 0 _ x = x
churchApply n f x = f (churchApply (n - 1) f x)

main :: IO ()
main = putStrLn ("church_3_successor_0=" ++ show (churchApply 3 (+1) 0))
