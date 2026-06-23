module Main where

placeValue :: [Int] -> Int
placeValue = foldl (\acc digit -> acc * 10 + digit) 0

main :: IO ()
main = putStrLn ("place_value_result=" ++ show (placeValue [1,2,3,0]))
