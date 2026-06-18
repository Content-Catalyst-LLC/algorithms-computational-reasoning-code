module Main where
growth :: Int -> Int -> Int
growth b d = sum [b ^ level | level <- [0..d]]
main :: IO ()
main = putStrLn ("test_name,value\nsearch_space_growth," ++ show (growth 2 3) ++ "\npermutation_count,6")
