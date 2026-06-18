module Main where
speedup :: Double -> Double -> Double
speedup s p = 1 / (s + ((1 - s) / p))
main :: IO ()
main = putStrLn ("test_name,value\nspeedup_p16_s010," ++ show (speedup 0.10 16) ++ "\nefficiency_p16_s010," ++ show ((speedup 0.10 16)/16))
