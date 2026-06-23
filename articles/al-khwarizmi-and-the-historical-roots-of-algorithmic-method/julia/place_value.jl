digits = [1, 2, 3, 0]
value = 0
for digit in digits
    global value = value * 10 + digit
end
println("place_value_result=", value)
