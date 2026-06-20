module Main where

score :: Double -> Double -> Double -> Double -> Double -> Double
score threatModel keys validation integrity authentication =
  100.0 * (0.22 * threatModel + 0.24 * keys + 0.18 * validation + 0.18 * integrity + 0.18 * authentication)

main :: IO ()
main = do
  putStrLn $ "standard secure channel score=" ++ show (score 0.86 0.82 0.90 0.86 0.84)
  putStrLn $ "legacy manual transfer score=" ++ show (score 0.36 0.24 0.18 0.34 0.28)
