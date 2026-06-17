module Main where

data LiteracyCase = LiteracyCase
  { name :: String
  , transparency :: Double
  , interpretability :: Double
  , contestability :: Double
  , governance :: Double
  , judgment :: Double
  } deriving (Show)

score :: LiteracyCase -> Double
score c =
  100 * (0.22 * transparency c + 0.22 * interpretability c + 0.18 * contestability c + 0.18 * governance c + 0.20 * judgment c)

main :: IO ()
main = do
  let cases =
        [ LiteracyCase "Search ranking" 0.62 0.66 0.38 0.52 0.68
        , LiteracyCase "Public decision-support workflow" 0.58 0.56 0.70 0.76 0.74
        , LiteracyCase "Scientific simulation dashboard" 0.76 0.74 0.60 0.68 0.80
        , LiteracyCase "Recommendation feed" 0.40 0.48 0.32 0.46 0.50
        ]
  putStrLn "case_name,literacy_support_score"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
