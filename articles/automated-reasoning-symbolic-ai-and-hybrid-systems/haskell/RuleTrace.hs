module Main where

facts :: [String]
facts = ["has_documentation", "logs_decisions"]

premises :: [String]
premises = ["has_documentation", "logs_decisions"]

fires :: Bool
fires = all (`elem` facts) premises

main :: IO ()
main = putStrLn ("rule_fires=" ++ show fires)
