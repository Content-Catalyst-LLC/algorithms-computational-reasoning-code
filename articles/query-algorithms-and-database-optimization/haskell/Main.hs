module Main where
selectionRows rows selectivity = rows * selectivity
joinRows l r ld rd = (l*r) / max ld rd
main = putStrLn ("test_name,value\nselection_estimated_rows," ++ show (selectionRows 1000000 0.012) ++ "\njoin_estimated_rows," ++ show (joinRows 500000 200000 50000 40000))
