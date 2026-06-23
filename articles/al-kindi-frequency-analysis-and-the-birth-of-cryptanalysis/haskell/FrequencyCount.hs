module Main where

import Data.Char (isAlpha, toLower)
import qualified Data.Map.Strict as M

main :: IO ()
main = do
  let text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE"
      symbols = map toLower (filter isAlpha text)
      counts = foldr (\c -> M.insertWith (+) c 1) M.empty symbols
  print counts
