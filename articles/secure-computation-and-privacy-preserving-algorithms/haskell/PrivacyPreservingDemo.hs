module Main where

updates :: [(Double, Double)]
updates = [(100, 0.42), (240, 0.55), (160, 0.49)]

federatedAverage :: [(Double, Double)] -> Double
federatedAverage xs = sum [n * w | (n, w) <- xs] / sum [n | (n, _) <- xs]

main :: IO ()
main = putStrLn $ "federated average weight=" ++ show (federatedAverage updates)
