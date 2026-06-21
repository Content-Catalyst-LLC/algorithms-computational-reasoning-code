module Main where

weights :: [Double]
weights = [0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03]

score :: Double
score = 100 * sum (map (*0.65) weights)

main :: IO ()
main = print score
