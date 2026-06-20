# Gradient descent teaching example in Julia.

data = [(-2.0, -2.85), (-1.0, -0.67), (0.0, 1.47), (1.0, 3.63), (2.0, 5.82)]

function mse(w, b)
    mean([(y - (w*x + b))^2 for (x, y) in data])
end

function step(w, b, eta)
    n = length(data)
    grad_w = sum([(2/n) * ((w*x + b) - y) * x for (x, y) in data])
    grad_b = sum([(2/n) * ((w*x + b) - y) for (x, y) in data])
    return w - eta * grad_w, b - eta * grad_b
end

w = 0.0
b = 0.0
eta = 0.08
for i in 1:80
    global w, b = step(w, b, eta)
end

println((weight=w, bias=b, loss=mse(w,b)))
