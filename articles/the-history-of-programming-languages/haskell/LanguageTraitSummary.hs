module Main where

languages :: [(String, String)]
languages =
  [ ("Fortran", "scientific numerical programming")
  , ("Lisp", "symbolic computation")
  , ("SQL", "declarative data querying")
  , ("Rust", "memory-safe systems programming")
  ]

main :: IO ()
main = mapM_ (\(lang, trait) -> putStrLn (lang ++ ": " ++ trait)) languages
