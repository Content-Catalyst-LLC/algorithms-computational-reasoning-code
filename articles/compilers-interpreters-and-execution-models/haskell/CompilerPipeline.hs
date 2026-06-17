module CompilerPipeline where
data Stage = SourceCode | Lexing | Parsing | SemanticAnalysis | IntermediateRepresentation | Optimization | CodeGeneration | Linking | Loading | Execution deriving (Eq, Show, Enum, Bounded)
pipeline :: [Stage]
pipeline = [minBound .. maxBound]
