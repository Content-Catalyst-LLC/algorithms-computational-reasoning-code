text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE"
counts = Dict{Char, Int}()
for ch in lowercase(text)
    if isletter(ch)
        counts[ch] = get(counts, ch, 0) + 1
    end
end
println(counts)
