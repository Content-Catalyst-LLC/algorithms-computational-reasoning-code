module Main where
factorial :: Int -> Int
factorial n = if n <= 0 then 1 else n * factorial (n - 1)
main :: IO ()
main = putStrLn ("test_name,value\nfactorial_5," ++ show (factorial 5) ++ "\niterative_sum,6")
