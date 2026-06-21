# Simulation as Computational Reasoning - Julia scaffold
stock = 100.0
for t in 0:30
    global stock
    println((time_step=t, stock=round(stock, digits=6)))
    stock = max(0.0, stock + 0.08stock - 0.03stock - 0.04stock)
end
