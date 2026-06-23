function bernoulli(n)
    a = [0//1 for _ in 0:n]
    for m in 0:n
        a[m + 1] = 1//(m + 1)
        for j in m:-1:1
            a[j] = j * (a[j] - a[j + 1])
        end
    end
    return a[1]
end

println("B_8=", bernoulli(8))
