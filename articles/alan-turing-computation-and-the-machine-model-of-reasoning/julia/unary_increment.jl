function unary_increment(tape)
    chars = collect(tape)
    i = 1
    while i <= length(chars) && chars[i] == '1'
        i += 1
    end
    if i > length(chars)
        push!(chars, '_')
    end
    chars[i] = '1'
    if i == length(chars)
        push!(chars, '_')
    end
    return join(chars)
end

println("incremented_tape=", unary_increment("111_"))
