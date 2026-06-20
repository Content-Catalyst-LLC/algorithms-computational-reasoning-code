module Main where
profiles :: [(String, String, Double, Double)]
profiles = [("cooperate", "cooperate", 3, 3), ("cooperate", "defect", 0, 5), ("defect", "cooperate", 5, 0), ("defect", "defect", 1, 1)]
main :: IO ()
main = mapM_ print profiles
