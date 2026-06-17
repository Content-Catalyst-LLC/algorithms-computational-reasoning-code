module TypeDiscipline where

newtype Slug = Slug String deriving (Eq, Show)
data PublicationStatus = Draft | Review | Published | Archived deriving (Eq, Show)
data ArticleRecord = ArticleRecord { title :: String, slug :: Slug, status :: PublicationStatus } deriving (Eq, Show)

validateSlug :: String -> Maybe Slug
validateSlug "" = Nothing
validateSlug s = Just (Slug s)
