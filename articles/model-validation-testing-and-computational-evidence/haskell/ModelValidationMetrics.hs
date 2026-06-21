module Main where

observed :: [Double]
observed = [33.1, 39.7, 38.8, 39.3, 8.4]

predicted :: [Double]
predicted = [31.92, 31.58, 36.48, 25.30, 11.30]

main :: IO ()
main = do
  let errors = zipWith (-) observed predicted
      n = fromIntegral (length errors)
      rmse = sqrt (sum (map (^ (2 :: Int)) errors) / n)
      mae = sum (map abs errors) / n
  putStrLn ("rmse=" ++ show rmse)
  putStrLn ("mae=" ++ show mae)
