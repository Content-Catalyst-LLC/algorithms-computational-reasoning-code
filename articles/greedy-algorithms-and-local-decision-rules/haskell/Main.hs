module Main where
intervalScheduling :: [(String, Int, Int)] -> [(String, Int, Int)]
intervalScheduling xs = go (sortByFinish xs) (-1000000) []
  where
    sortByFinish = foldr insert []
    insert x [] = [x]
    insert x (y:ys) | finish x <= finish y = x:y:ys
                    | otherwise = y : insert x ys
    finish (_,_,f) = f
    go [] _ acc = reverse acc
    go (i@(_,s,f):rest) cur acc
      | s >= cur = go rest f (i:acc)
      | otherwise = go rest cur acc
main :: IO ()
main = putStrLn ("test_name,value\ninterval_count," ++ show (length (intervalScheduling [("A",0,6),("B",1,4),("C",5,7)])))
