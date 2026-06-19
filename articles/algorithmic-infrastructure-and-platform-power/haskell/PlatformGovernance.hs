module PlatformGovernance where
data PlatformControl = AccessControl | Ranking | RateLimit | DataExport | AuditTrail | AppealMechanism deriving (Eq, Show)
