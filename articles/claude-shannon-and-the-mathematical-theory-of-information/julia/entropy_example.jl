function entropy(probs)
    return -sum(p > 0 ? p * log2(p) : 0.0 for p in probs)
end

println("entropy_bits=", entropy([0.5, 0.5]))
