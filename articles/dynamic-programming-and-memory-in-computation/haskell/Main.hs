module Main where
fib :: Int -> Int
fib n = fibs !! n where fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
main :: IO ()
main = putStrLn ("test_name,value\nfibonacci_10," ++ show (fib 10) ++ "\nstate_space_size,100000")
