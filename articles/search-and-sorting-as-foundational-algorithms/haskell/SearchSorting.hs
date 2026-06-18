module SearchSorting where
linearSearch :: Eq a => [a] -> a -> Maybe Int
linearSearch xs target = go 0 xs where
  go _ [] = Nothing
  go i (y:ys) | y == target = Just i
              | otherwise = go (i+1) ys
