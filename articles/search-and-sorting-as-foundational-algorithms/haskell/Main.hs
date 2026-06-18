module Main where
linearSearch :: Eq a => [a] -> a -> Maybe Int
linearSearch xs target = go 0 xs where
  go _ [] = Nothing
  go i (y:ys) | y == target = Just i
              | otherwise = go (i+1) ys
main :: IO ()
main = putStrLn ("test_name,value\nlinear_search_9," ++ show (linearSearch [7,2,9,1] 9) ++ "\nsort_demo,[1,2,7,9]")
