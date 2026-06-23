pd = 0.035
lgd = 0.45
ead = 100000.0
expected_loss = pd * lgd * ead
println("expected_loss=", round(expected_loss, digits=4))
