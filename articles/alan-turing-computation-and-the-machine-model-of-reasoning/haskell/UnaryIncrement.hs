module Main where

unaryIncrement :: String -> String
unaryIncrement [] = "1_"
unaryIncrement ('1':xs) = '1' : unaryIncrement xs
unaryIncrement ('_':xs) = '1' : '_' : xs
unaryIncrement xs = xs

main :: IO ()
main = putStrLn ("incremented_tape=" ++ unaryIncrement "111_")
