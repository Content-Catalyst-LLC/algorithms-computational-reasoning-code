module DataQuality where
data QualityDimension = Completeness | Accuracy | Consistency | Timeliness | Validity | Provenance | Representativeness deriving (Eq, Show)
