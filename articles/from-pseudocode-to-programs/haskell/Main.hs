module Main where

data TranslationCase = TranslationCase
  { name :: String
  , intent :: Double
  , control :: Double
  , edge :: Double
  , tests :: Double
  , maintain :: Double
  } deriving (Show)

score :: TranslationCase -> Double
score c =
  100 * (0.22 * intent c + 0.22 * control c + 0.18 * edge c + 0.18 * tests c + 0.20 * maintain c)

main :: IO ()
main = do
  let cases =
        [ TranslationCase "Search ranking prototype" 0.82 0.80 0.64 0.68 0.72
        , TranslationCase "Decision-rule implementation" 0.76 0.74 0.66 0.62 0.68
        , TranslationCase "Simulation loop" 0.84 0.82 0.72 0.70 0.74
        , TranslationCase "Data-cleaning procedure" 0.78 0.76 0.70 0.66 0.72
        ]
  putStrLn "case_name,translation_quality"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
