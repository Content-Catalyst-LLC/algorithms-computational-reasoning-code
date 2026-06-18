module Main where
relativeGap :: Double -> Double -> Double
relativeGap alg bound = (alg - bound) / bound
main :: IO ()
main = putStrLn ("test_name,value\nrelative_gap," ++ show (relativeGap 12 10) ++ "\napproximation_ratio,1.5")
