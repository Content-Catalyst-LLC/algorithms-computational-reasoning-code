module Main where

step :: Double -> Double -> Double -> Double
step target gain x = x - gain * (x - target)

run :: Int -> Double -> Double -> Double -> Double
run 0 _ _ x = x
run n target gain x = run (n - 1) target gain (step target gain x)

main :: IO ()
main = putStrLn ("final_state=" ++ show (run 5 0.0 0.2 10.0))
