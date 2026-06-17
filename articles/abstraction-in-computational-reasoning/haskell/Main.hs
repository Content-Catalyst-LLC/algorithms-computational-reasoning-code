module Main where

data AbstractionCase = AbstractionCase
  { name :: String
  , clarity :: Double
  , scope :: Double
  , detail :: Double
  , interpretation :: Double
  , governance :: Double
  } deriving (Show)

score :: AbstractionCase -> Double
score c =
  100 * (0.22 * clarity c + 0.20 * scope c + 0.20 * detail c + 0.23 * interpretation c + 0.15 * governance c)

main :: IO ()
main = do
  let cases =
        [ AbstractionCase "Search ranking" 0.82 0.70 0.62 0.60 0.56
        , AbstractionCase "Transit model" 0.78 0.72 0.66 0.72 0.66
        , AbstractionCase "Database schema" 0.84 0.78 0.70 0.74 0.70
        , AbstractionCase "Decision-support score" 0.70 0.60 0.48 0.52 0.66
        ]
  putStrLn "case_name,abstraction_score"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
