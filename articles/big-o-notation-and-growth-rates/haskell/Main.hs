module Main where
nlogn :: Double -> Double
nlogn n = n * logBase 2 n
main :: IO ()
main = putStrLn ("test_name,value\nlinear_1000,1000\nnlogn_1000," ++ show (nlogn 1000) ++ "\nquadratic_1000,1000000")
