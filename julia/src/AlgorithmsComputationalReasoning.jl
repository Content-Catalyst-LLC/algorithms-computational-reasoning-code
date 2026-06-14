module AlgorithmsComputationalReasoning

export growth_table

function growth_table(ns)
    return [(n=n, linear=n, quadratic=n^2) for n in ns]
end

end
