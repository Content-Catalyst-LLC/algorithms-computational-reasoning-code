module Main where

teachingChecksum :: String -> Int
teachingChecksum s = sum (zipWith (*) (map fromEnum s) [1..]) `mod` 1000003

main :: IO ()
main = do
  let original = "verified artifact manifest"
  let altered = "verified artifact manifest!"
  putStrLn $ "original checksum=" ++ show (teachingChecksum original)
  putStrLn $ "altered checksum=" ++ show (teachingChecksum altered)
  putStrLn $ "match=" ++ show (teachingChecksum original == teachingChecksum altered)
