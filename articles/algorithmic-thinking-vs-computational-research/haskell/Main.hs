module Main where

data Profile = Profile
  { name :: String
  , stepClarity :: Double
  , decomposition :: Double
  , controlFlow :: Double
  , testability :: Double
  , representation :: Double
  , governance :: Double
  } deriving (Show)

algorithmicScore :: Profile -> Double
algorithmicScore p = 100 * (0.28 * stepClarity p + 0.24 * decomposition p + 0.24 * controlFlow p + 0.24 * testability p)

computationalScore :: Profile -> Double
computationalScore p = 100 * (0.16 * stepClarity p + 0.14 * decomposition p + 0.14 * controlFlow p + 0.14 * testability p + 0.22 * representation p + 0.20 * governance p)

main :: IO ()
main = do
  let profiles =
        [ Profile "Recipe-like procedure" 0.86 0.72 0.70 0.62 0.42 0.20
        , Profile "Classroom algorithm exercise" 0.90 0.82 0.84 0.78 0.62 0.32
        , Profile "Search and ranking system" 0.72 0.70 0.76 0.66 0.78 0.70
        , Profile "Public decision-support workflow" 0.68 0.66 0.64 0.72 0.80 0.86
        , Profile "Scientific modeling workflow" 0.74 0.78 0.76 0.82 0.86 0.74
        ]
  putStrLn "name,algorithmic_score,computational_score"
  mapM_ (\p -> putStrLn (name p ++ "," ++ show (algorithmicScore p) ++ "," ++ show (computationalScore p))) profiles
