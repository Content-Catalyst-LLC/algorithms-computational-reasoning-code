data ProxyRisk = Low | Medium | High deriving (Show, Eq)
review :: ProxyRisk -> String
review High = "requires governance review"
review Medium = "requires documentation"
review Low = "monitor"
main :: IO ()
main = putStrLn (review High)
