module OrderingRules where
nondecreasing :: Ord a => [a] -> Bool
nondecreasing xs = and (zipWith (<=) xs (drop 1 xs))
