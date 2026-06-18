function binary_search(values, target)
    lo = 1; hi = length(values)
    while lo <= hi
        mid = fld(lo + hi, 2)
        values[mid] == target && return mid
        values[mid] < target ? (lo = mid + 1) : (hi = mid - 1)
    end
    return 0
end
println("test_name,value")
println("binary_search_5,$(binary_search([1,2,5,9], 5))")
println("sort_demo,$(join(sort([7,2,9,1]), ':'))")
