-- Compact Haskell example: typed intervention comparison.
data Decision = Act | Monitor deriving (Show, Eq)

decide :: Double -> Double -> Decision
decide threshold score = if score >= threshold then Act else Monitor

effect :: Double -> Double -> Double
effect baseline intervention = intervention - baseline

main :: IO ()
main = do
  let baseline = 0.42
      intervention = 0.57
      score = 0.53
  print (effect baseline intervention)
  print (decide 0.55 score, decide 0.50 score)
