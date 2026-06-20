module Main where
edgeCount :: Int
edgeCount = 7
nodeCount :: Int
nodeCount = 5
density :: Double
density = fromIntegral edgeCount / fromIntegral (nodeCount * (nodeCount - 1))
main :: IO ()
main = putStrLn ("test_name,value\nnode_count," ++ show nodeCount ++ "\nedge_count," ++ show edgeCount ++ "\ndensity," ++ show density ++ "\nmanual_shortest_path_cost,5.5")
