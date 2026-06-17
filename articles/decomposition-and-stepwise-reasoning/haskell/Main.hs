module Main where

data DecompositionCase = DecompositionCase
  { name :: String
  , subproblem :: Double
  , boundary :: Double
  , sequencing :: Double
  , dependencies :: Double
  , recomposition :: Double
  } deriving (Show)

score :: DecompositionCase -> Double
score c =
  100 * (0.22 * subproblem c + 0.20 * boundary c + 0.18 * sequencing c + 0.20 * dependencies c + 0.20 * recomposition c)

main :: IO ()
main = do
  let cases =
        [ DecompositionCase "Search system" 0.82 0.78 0.82 0.72 0.72
        , DecompositionCase "Public decision-support workflow" 0.74 0.66 0.68 0.60 0.58
        , DecompositionCase "Scientific simulation" 0.86 0.82 0.80 0.78 0.82
        , DecompositionCase "Knowledge architecture" 0.80 0.76 0.74 0.70 0.80
        ]
  putStrLn "case_name,decomposition_score"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
