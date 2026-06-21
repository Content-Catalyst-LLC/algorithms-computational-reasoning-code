module Main where

data Contrast = Contrast { treatedMean :: Double, controlMean :: Double }

effect :: Contrast -> Double
effect c = treatedMean c - controlMean c

main :: IO ()
main = do
  let c = Contrast 0.64 0.47
  putStrLn ("causal contrast = " ++ show (effect c))
