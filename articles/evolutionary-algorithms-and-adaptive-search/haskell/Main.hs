module Main where
binaryFitness :: [Int] -> Int
binaryFitness = sum
main :: IO ()
main = putStrLn ("test_name,value\nbinary_fitness," ++ show (binaryFitness [1,0,1,1]) ++ "\nmutation_rate,0.03")
