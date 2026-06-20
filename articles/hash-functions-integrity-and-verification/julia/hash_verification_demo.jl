# Hash verification teaching demo in Julia.
# Uses only Base; this is a teaching checksum, not cryptographic hashing.
function teaching_checksum(s::AbstractString)
    total = 0
    for (i, c) in enumerate(codeunits(s))
        total = (total + Int(c) * i) % 1000003
    end
    return total
end

original = "verified artifact manifest"
altered = "verified artifact manifest!"
println("original checksum=", teaching_checksum(original))
println("altered checksum=", teaching_checksum(altered))
println("match=", teaching_checksum(original) == teaching_checksum(altered))
