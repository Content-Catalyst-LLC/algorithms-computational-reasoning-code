module QueryLogic where
data Predicate = Equals String String | Exists String | NotExists String deriving (Eq, Show)
