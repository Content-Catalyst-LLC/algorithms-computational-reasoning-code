f(x) = sin(x) + 0.25x^2
central_difference(x, h) = (f(x + h) - f(x - h)) / (2h)
println(central_difference(1.0, 0.01))
