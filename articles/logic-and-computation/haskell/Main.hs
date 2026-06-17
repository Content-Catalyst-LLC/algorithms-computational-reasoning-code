module Main where

data LogicCase = LogicCase
  { name :: String
  , ruleClarity :: Double
  , predicateDefinition :: Double
  , traceability :: Double
  , testability :: Double
  , governance :: Double
  } deriving (Show)

score :: LogicCase -> Double
score c =
  100 * (0.24 * ruleClarity c + 0.24 * predicateDefinition c + 0.20 * traceability c + 0.18 * testability c + 0.14 * governance c)

main :: IO ()
main = do
  let cases =
        [ LogicCase "Input validation rules" 0.82 0.84 0.68 0.82 0.70
        , LogicCase "Database query constraints" 0.78 0.80 0.72 0.76 0.72
        , LogicCase "Decision-rule workflow" 0.74 0.70 0.68 0.72 0.78
        , LogicCase "Program invariant checks" 0.80 0.78 0.74 0.80 0.66
        ]
  putStrLn "case_name,logic_quality"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
