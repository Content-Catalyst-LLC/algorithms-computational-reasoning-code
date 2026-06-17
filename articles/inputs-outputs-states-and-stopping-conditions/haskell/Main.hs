module Main where

data BoundaryCase = BoundaryCase
  { name :: String
  , input :: Double
  , output :: Double
  , state :: Double
  , stopping :: Double
  , failure :: Double
  } deriving (Show)

score :: BoundaryCase -> Double
score c =
  100 * (0.22 * input c + 0.22 * output c + 0.22 * state c + 0.20 * stopping c + 0.14 * failure c)

main :: IO ()
main = do
  let cases =
        [ BoundaryCase "Graph traversal" 0.84 0.80 0.86 0.80 0.70
        , BoundaryCase "Decision-support workflow" 0.68 0.70 0.74 0.62 0.60
        , BoundaryCase "Numerical simulation" 0.82 0.78 0.84 0.78 0.66
        , BoundaryCase "Recommendation ranking" 0.74 0.72 0.70 0.60 0.52
        ]
  putStrLn "case_name,boundary_score"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
