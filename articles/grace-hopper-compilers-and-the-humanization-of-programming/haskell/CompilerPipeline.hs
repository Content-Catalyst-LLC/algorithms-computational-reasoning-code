module Main where

main :: IO ()
main = do
  let source = "ADD PAYROLL-TOTAL TO TAX-BASE"
  let tokens = words source
  putStrLn ("source=" ++ source)
  putStrLn ("tokens=" ++ show tokens)
  putStrLn "target_code=machine-specific instruction sequence"
