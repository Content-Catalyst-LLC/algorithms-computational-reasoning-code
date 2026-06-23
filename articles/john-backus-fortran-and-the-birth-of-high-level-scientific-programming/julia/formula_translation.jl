function formula(x, a, b, c)
    return a*x*x + b*x + c
end

for x in [-2, -1, 0, 1, 2, 3]
    println("x=", x, ", y=", formula(x, 2, -3, 1))
end
