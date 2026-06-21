status :: Double -> String -> String
status score stakes
  | stakes == "high" && score < 1.0 = "escalate"
  | score >= 0.8 = "pass"
  | otherwise = "review"

main :: IO ()
main = putStrLn (status 0.67 "medium")
