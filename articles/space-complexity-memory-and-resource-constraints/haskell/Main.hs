module Main where
matrixUnits :: Integer -> Integer
matrixUnits v = v * v
adjacencyListUnits :: Integer -> Integer -> Integer
adjacencyListUnits v e = v + e
main :: IO ()
main = putStrLn ("test_name,value\nmatrix_units," ++ show (matrixUnits 1000) ++ "\nadjacency_list_units," ++ show (adjacencyListUnits 1000 5000))
