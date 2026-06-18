module DataPipelines where
data PipelineStage = Source | Ingestion | Validation | Transformation | Enrichment | Storage | Delivery | Monitoring deriving (Eq, Show)
