module Main where

formula :: Double -> Double -> Double -> Double -> Double
formula x a b c = a*x*x + b*x + c

main :: IO ()
main = mapM_ (\x -> putStrLn ("x=" ++ show x ++ ", y=" ++ show (formula x 2 (-3) 1))) [-2,-1,0,1,2,3]
