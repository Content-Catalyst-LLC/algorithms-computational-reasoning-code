module Main where
verifyColoring :: [(Int,Int)] -> [(Int,Int)] -> Bool
verifyColoring edges colors = all (\(u,v) -> lookup u colors /= lookup v colors) edges
main :: IO ()
main = putStrLn ("test_name,value\ncoloring_valid," ++ show (verifyColoring [(1,2),(2,3)] [(1,1),(2,2),(3,1)]))
