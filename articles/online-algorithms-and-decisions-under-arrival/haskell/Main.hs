module Main where
skiRental :: Double -> Double -> Int -> (Double, Double, Double)
skiRental rent buy days =
  let breakEven = floor (buy / rent)
      rentOnly = fromIntegral days * rent
      buyNow = buy
      threshold = (fromIntegral (min days breakEven) * rent) + if days > breakEven then buy else 0
      offline = min rentOnly buyNow
  in (threshold, offline, threshold / offline)
main :: IO ()
main = let (t,o,r)=skiRental 10 50 8 in putStrLn ("test_name,value\nthreshold_strategy," ++ show t ++ "\noffline_optimum," ++ show o ++ "\nratio," ++ show r)
