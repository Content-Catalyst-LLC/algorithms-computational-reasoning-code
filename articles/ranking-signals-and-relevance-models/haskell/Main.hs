module Main where
precisionAtK :: Double -> Double -> Double
precisionAtK tp k = if k == 0 then 0 else tp / k
rankingScore :: Double -> Double -> Double -> Double -> Double -> Double -> Double
rankingScore lexical metadata freshness authority semantic provenance =
  100 * (0.22*lexical + 0.18*metadata + 0.12*freshness + 0.16*authority + 0.17*semantic + 0.15*provenance)
main :: IO ()
main = putStrLn ("test_name,value\nprecision_at_3," ++ show (precisionAtK 2 3) ++ "\nranking_signal_score," ++ show (rankingScore 0.84 0.88 0.76 0.82 0.78 0.86))
