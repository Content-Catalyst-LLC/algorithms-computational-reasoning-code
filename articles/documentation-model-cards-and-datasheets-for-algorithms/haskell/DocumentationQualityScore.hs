module Main where

main :: IO ()
main = do
  let scores = [0.62, 0.6875, 0.58, 0.50, 0.56, 0.52]
      quality = sum scores / fromIntegral (length scores)
  putStrLn ("documentation_quality_score=" ++ show quality)
