module Main where

clamp :: Double -> Double
clamp x = max 0 (min 1 x)

model :: Double -> Double -> Double -> Double -> Double
model demand capacity failure adaptation = clamp (0.5 + 0.30*demand + 0.25*failure - 0.20*capacity - 0.15*adaptation)

main :: IO ()
main = putStrLn ("baseline_risk=" ++ show (model 0.45 0.35 0.25 0.30))
