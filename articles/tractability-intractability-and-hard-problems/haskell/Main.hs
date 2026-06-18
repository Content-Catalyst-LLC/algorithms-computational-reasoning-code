module Main where
subsetCount :: Integer -> Integer
subsetCount n = 2 ^ n
main :: IO ()
main = putStrLn ("test_name,value\nsubsets_20," ++ show (subsetCount 20) ++ "\npairs_100,4950")
