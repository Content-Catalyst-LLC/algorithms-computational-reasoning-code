module Main where

data Alternative = Alternative { name :: String, cost :: Double, risk :: Double, quality :: Double } deriving Show

alts :: [Alternative]
alts = [ Alternative "A" 72 34 82, Alternative "B" 64 41 76, Alternative "C" 81 26 88, Alternative "D" 58 52 69 ]

normMin :: Double -> [Double] -> Double
normMin x xs = if maximum xs == minimum xs then 1 else (maximum xs - x) / (maximum xs - minimum xs)

normMax :: Double -> [Double] -> Double
normMax x xs = if maximum xs == minimum xs then 1 else (x - minimum xs) / (maximum xs - minimum xs)

score :: Alternative -> Double
score a = 0.35 * normMin (cost a) (map cost alts) + 0.30 * normMin (risk a) (map risk alts) + 0.35 * normMax (quality a) (map quality alts)

main :: IO ()
main = mapM_ print [(name a, score a) | a <- alts]
