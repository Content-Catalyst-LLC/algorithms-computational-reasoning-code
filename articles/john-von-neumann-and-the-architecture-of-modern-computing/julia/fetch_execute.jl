program = [("LOAD", 2), ("ADD", 3), ("STORE", 0), ("HALT", 0)]
acc = 0
for (op, arg) in program
    if op == "LOAD"
        global acc = arg
    elseif op == "ADD"
        global acc += arg
    elseif op == "STORE"
        println("store address=", arg, " value=", acc)
    elseif op == "HALT"
        println("halt accumulator=", acc)
        break
    end
end
