module Main where
precision :: Double -> Double -> Double
precision tp retrieved = if retrieved == 0 then 0 else tp / retrieved
recall :: Double -> Double -> Double
recall tp relevant = if relevant == 0 then 0 else tp / relevant
main :: IO ()
main = putStrLn ("test_name,value\nprecision," ++ show (precision 2 3) ++ "\nrecall," ++ show (recall 2 2))
