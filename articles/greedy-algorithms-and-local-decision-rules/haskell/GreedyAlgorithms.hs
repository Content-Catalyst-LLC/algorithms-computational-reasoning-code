module GreedyAlgorithms where
chooseMax :: Ord a => [a] -> Maybe a
chooseMax [] = Nothing
chooseMax xs = Just (maximum xs)
