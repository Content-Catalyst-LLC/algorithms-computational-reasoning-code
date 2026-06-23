for n in [10, 100, 1000, 10000]
    println("n=", n, " log2=", log2(n), " nlogn=", n*log2(n), " n2=", n*n)
end
