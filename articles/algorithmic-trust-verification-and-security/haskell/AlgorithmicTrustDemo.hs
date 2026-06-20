module Main where

trustQuality :: Double -> Double -> Double -> Double -> Double -> Double -> Double
trustQuality verification validation security provenance monitoring governance =
  100 * (0.18*verification + 0.18*validation + 0.18*security + 0.16*provenance + 0.15*monitoring + 0.15*governance)

main :: IO ()
main = putStrLn $ "trust quality=" ++ show (trustQuality 0.88 0.82 0.88 0.90 0.84 0.82)
