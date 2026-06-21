# Scientific computing approximation examples in Julia.
f(x) = sin(x)
central_difference(x, h) = (f(x + h) - f(x - h)) / (2h)
trapezoid(n) = begin
    a = 0.0; b = pi; h = (b - a) / n
    xs = range(a, b, length=n+1)
    ys = sin.(xs)
    h * (0.5 * first(ys) + sum(ys[2:end-1]) + 0.5 * last(ys))
end
println((derivative=central_difference(1.0, 1e-4), integral=trapezoid(200)))
