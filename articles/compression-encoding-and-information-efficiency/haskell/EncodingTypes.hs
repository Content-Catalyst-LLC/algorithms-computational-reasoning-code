module EncodingTypes where

type Symbol = Char
type Codeword = String

data CompressionMode = Lossless | Lossy deriving (Eq, Show)
data RepresentationEvidence = RepresentationEvidence { formatName :: String, encoding :: String, mode :: CompressionMode } deriving (Eq, Show)
