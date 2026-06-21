module Main where

data Decision = Favorable | NotFavorable deriving (Eq, Show)

label :: Double -> Double -> Decision
label threshold score = if score >= threshold then Favorable else NotFavorable

flipped :: Double -> Double -> Double -> Bool
flipped threshold original counterfactual = label threshold original /= label threshold counterfactual

main :: IO ()
main = print (flipped 0.62 0.57 0.65)
