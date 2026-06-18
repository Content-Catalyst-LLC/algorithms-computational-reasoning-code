module Main where
schemaQuality :: Double -> Double -> Double -> Double -> Double -> Double
schemaQuality fields keys constraints metadata lineage = 100 * (0.22*fields + 0.20*keys + 0.20*constraints + 0.20*metadata + 0.18*lineage)
main :: IO ()
main = putStrLn ("test_name,value\nschema_quality_score," ++ show (schemaQuality 0.90 0.85 0.80 0.88 0.82))
