module Main where
amplification :: Double -> Int -> Double
amplification p k = p ^ k
main :: IO ()
main = putStrLn ("test_name,value\namplification_failure," ++ show (amplification 0.1 5) ++ "\nseed,20260617")
