module Main where

data FormalizationCase = FormalizationCase
  { name :: String
  , inputClarity :: Double
  , outputClarity :: Double
  , objectiveAlignment :: Double
  , assumptionDocumentation :: Double
  , governanceReadiness :: Double
  } deriving (Show)

score :: FormalizationCase -> Double
score c =
  100 * (0.20 * inputClarity c + 0.20 * outputClarity c + 0.25 * objectiveAlignment c + 0.20 * assumptionDocumentation c + 0.15 * governanceReadiness c)

main :: IO ()
main = do
  let cases =
        [ FormalizationCase "Document search" 0.82 0.78 0.70 0.58 0.56
        , FormalizationCase "Worker scheduling" 0.72 0.76 0.58 0.54 0.62
        , FormalizationCase "Public service triage" 0.60 0.72 0.52 0.46 0.66
        , FormalizationCase "Scientific simulation" 0.86 0.80 0.76 0.84 0.70
        ]
  putStrLn "case_name,formalization_score"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
