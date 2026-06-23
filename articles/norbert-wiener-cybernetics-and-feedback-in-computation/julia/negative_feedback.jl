function negative_feedback(initial, target, gain, steps)
    x = initial
    for _ in 1:steps
        x = x - gain * (x - target)
    end
    return x
end

println("final_state=", negative_feedback(10.0, 0.0, 0.2, 5))
