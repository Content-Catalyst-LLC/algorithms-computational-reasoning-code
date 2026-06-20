# Dependency-light Julia example: transparent two-variable LP grid search.
function feasible(x, y; labor_limit=8, material_limit=8)
    return 2x + y <= labor_limit && x + 2y <= material_limit && x >= 0 && y >= 0
end

function objective(x, y)
    return 3x + 4y
end

best = nothing
for x in 0:9, y in 0:9
    if feasible(x, y)
        row = (x=x, y=y, objective=objective(x, y), labor=2x+y, material=x+2y)
        if best === nothing || row.objective > best.objective
            global best = row
        end
    end
end

println(best)
