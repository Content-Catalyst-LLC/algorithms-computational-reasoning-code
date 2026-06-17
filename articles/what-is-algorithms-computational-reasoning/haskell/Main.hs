module Main where

data Scenario = Scenario
  { name :: String
  , representation :: Double
  , correctness :: Double
  , governance :: Double
  , bruteForcePressure :: Double
  } deriving (Show)

score :: Scenario -> Double
score s = max 0 (min 100 (100 * (0.30 * representation s + 0.30 * correctness s + 0.30 * governance s - 0.10 * bruteForcePressure s)))

main :: IO ()
main = do
  let scenarios =
        [ Scenario "Brute-force procedure" 0.40 0.28 0.20 0.92
        , Scenario "Indexed search design" 0.62 0.52 0.38 0.42
        , Scenario "Graph-aware reasoning" 0.76 0.68 0.54 0.30
        , Scenario "Governed computational reasoning" 0.86 0.82 0.86 0.18
        ]
  mapM_ (\s -> putStrLn (name s ++ "," ++ show (score s))) scenarios
