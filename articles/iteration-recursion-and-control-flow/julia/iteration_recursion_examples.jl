function factorial_recursive(n)
    n < 0 && error("n must be nonnegative")
    n == 0 && return 1
    return n * factorial_recursive(n - 1)
end
println("test_name,value")
println("factorial_5,$(factorial_recursive(5))")
println("iterative_sum,$(sum([1,2,3]))")
