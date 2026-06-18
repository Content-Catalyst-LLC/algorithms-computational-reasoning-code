module RecurrenceExamples where
depthHalving :: Int -> Int
depthHalving n | n <= 1 = 0
               | otherwise = 1 + depthHalving (n `div` 2)
