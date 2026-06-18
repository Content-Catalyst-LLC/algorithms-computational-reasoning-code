function ski_rental(rent_cost, buy_cost, days)
    break_even = floor(Int, buy_cost / rent_cost)
    rent_only = days * rent_cost
    buy_now = buy_cost
    threshold = min(days, break_even) * rent_cost
    if days > break_even
        threshold += buy_cost
    end
    offline = min(rent_only, buy_now)
    return (threshold=threshold, offline=offline, ratio=threshold/offline)
end
row = ski_rental(10.0, 50.0, 8)
println("test_name,value")
println("threshold_strategy,$(row.threshold)")
println("offline_optimum,$(row.offline)")
println("ratio,$(row.ratio)")
