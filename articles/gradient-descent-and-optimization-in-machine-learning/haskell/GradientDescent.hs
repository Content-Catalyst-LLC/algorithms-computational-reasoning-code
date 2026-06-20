module Main where

data Point = Point Double Double deriving Show

dataSet :: [Point]
dataSet = [Point (-2) (-2.85), Point (-1) (-0.67), Point 0 1.47, Point 1 3.63, Point 2 5.82]

predictY :: Double -> Double -> Double -> Double
predictY w b x = w * x + b

mse :: Double -> Double -> Double
mse w b = sum [ (y - predictY w b x) ^ (2 :: Int) | Point x y <- dataSet ] / fromIntegral (length dataSet)

step :: Double -> (Double, Double) -> (Double, Double)
step eta (w,b) =
  let n = fromIntegral (length dataSet)
      gradW = sum [ (2 / n) * ((predictY w b x) - y) * x | Point x y <- dataSet ]
      gradB = sum [ (2 / n) * ((predictY w b x) - y) | Point x y <- dataSet ]
  in (w - eta * gradW, b - eta * gradB)

train :: Int -> Double -> (Double, Double)
train steps eta = iterate (step eta) (0,0) !! steps

main :: IO ()
main = do
  let (w,b) = train 80 0.08
  putStrLn $ "weight=" ++ show w ++ ", bias=" ++ show b ++ ", loss=" ++ show (mse w b)
