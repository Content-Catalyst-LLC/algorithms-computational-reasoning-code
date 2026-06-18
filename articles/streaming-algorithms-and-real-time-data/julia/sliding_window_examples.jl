items = ["A","B","A","C","A","D"]
window_size = 3
println("time,event,window")
for t in 1:length(items)
    start = max(1, t - window_size + 1)
    window = items[start:t]
    println("$(t),$(items[t]),$(join(window, "|"))")
end
