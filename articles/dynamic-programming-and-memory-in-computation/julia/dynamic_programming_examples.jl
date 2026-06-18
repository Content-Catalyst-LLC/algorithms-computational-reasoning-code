function fib_memo(n, memo=Dict{Int,Int}())
    haskey(memo, n) && return memo[n]
    memo[n] = n <= 1 ? n : fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
end
println("test_name,value")
println("fibonacci_10,$(fib_memo(10))")
println("state_space_size,$(100*50*20)")
