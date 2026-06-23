function gcd_algorithm(a, b)
    while b != 0
        a, b = b, a % b
    end
    return abs(a)
end

println("gcd=", gcd_algorithm(252, 105))
