module IdentityAccess

export identity_access_score

const WEIGHTS = Dict(
    "authentication_strength" => 0.10,
    "authorization_granularity" => 0.11,
    "least_privilege_alignment" => 0.11,
    "session_token_control" => 0.09,
    "machine_identity_governance" => 0.09,
    "audit_logging" => 0.10,
    "access_lifecycle_review" => 0.09,
    "privilege_escalation_controls" => 0.09,
    "privacy_and_inclusion_review" => 0.08,
    "incident_response" => 0.06,
    "governance_ownership" => 0.06,
    "communication_clarity" => 0.02
)

function identity_access_score(values::Dict{String,Float64})
    total = 0.0
    for (key, weight) in WEIGHTS
        total += get(values, key, 0.0) * weight
    end
    return 100.0 * total
end

if abspath(PROGRAM_FILE) == @__FILE__
    example = Dict(k => 0.75 for k in keys(WEIGHTS))
    println(identity_access_score(example))
end

end
