module Main where

data DebugCase = DebugCase
  { name :: String
  , reproduce :: Double
  , traceQuality :: Double
  , isolation :: Double
  , verification :: Double
  , regression :: Double
  } deriving (Show)

score :: DebugCase -> Double
score c =
  100 * (0.22 * reproduce c + 0.20 * traceQuality c + 0.18 * isolation c + 0.22 * verification c + 0.18 * regression c)

main :: IO ()
main = do
  let cases =
        [ DebugCase "Graph traversal infinite loop" 0.88 0.78 0.80 0.82 0.78
        , DebugCase "Data pipeline missing-value bug" 0.84 0.74 0.72 0.76 0.74
        , DebugCase "Simulation instability" 0.80 0.78 0.70 0.74 0.66
        , DebugCase "Recommendation ranking tie bug" 0.76 0.68 0.70 0.72 0.70
        ]
  putStrLn "case_name,debugging_quality"
  mapM_ (\c -> putStrLn (name c ++ "," ++ show (score c))) cases
