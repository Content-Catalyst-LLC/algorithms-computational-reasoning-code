rate :: Double -> Double -> Double -> Double -> (Double, Double, Double)
rate tp fp tn fn = (accuracy, precision, recall)
  where
    total = max 1 (tp + fp + tn + fn)
    accuracy = (tp + tn) / total
    precision = tp / max 1 (tp + fp)
    recall = tp / max 1 (tp + fn)

main :: IO ()
main = do
  let (accuracy, precision, recallValue) = rate 80 25 140 35
  putStrLn ("accuracy=" ++ show accuracy)
  putStrLn ("precision=" ++ show precision)
  putStrLn ("recall=" ++ show recallValue)
