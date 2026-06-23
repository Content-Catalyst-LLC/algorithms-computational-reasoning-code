church_apply(n, f, x) = foldl((acc, _) -> f(acc), 1:n; init=x)
println("church_3_successor_0=", church_apply(3, x -> x + 1, 0))
