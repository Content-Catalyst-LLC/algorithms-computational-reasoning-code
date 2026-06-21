module Main where

status :: Double -> Bool -> Bool -> String
status risk approvalRequired approved
  | approvalRequired && not approved = "blocked"
  | risk >= 0.65 = "escalate"
  | otherwise = "pass"

main :: IO ()
main = putStrLn ("agent_action_status=" ++ status 0.85 True False)
