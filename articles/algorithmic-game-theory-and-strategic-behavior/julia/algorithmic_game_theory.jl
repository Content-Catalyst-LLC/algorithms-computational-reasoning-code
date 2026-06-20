payoffs = Dict(
    ("cooperate", "cooperate") => (3.0, 3.0),
    ("cooperate", "defect") => (0.0, 5.0),
    ("defect", "cooperate") => (5.0, 0.0),
    ("defect", "defect") => (1.0, 1.0)
)
for profile in sort(collect(keys(payoffs)))
    println(profile, " => ", payoffs[profile])
end
