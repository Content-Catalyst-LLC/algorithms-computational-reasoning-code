x0, y0 = 10.0, 1.2
x1, y1 = 20.0, 2.8
x = 15.0
y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0)
println("interpolated_y=", y)
