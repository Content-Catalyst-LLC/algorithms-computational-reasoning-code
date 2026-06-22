module Main where

main :: IO ()
main = do
  let scores = [0.70, 0.74, 0.62, 0.58, 0.46]
      quality = sum scores / fromIntegral (length scores)
  putStrLn ("explanation_quality_score=" ++ show quality)
