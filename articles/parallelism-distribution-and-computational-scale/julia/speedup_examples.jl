speedup(serial_fraction, p) = 1.0 / (serial_fraction + ((1.0 - serial_fraction) / p))
println("test_name,value")
println("speedup_p16_s010,$(speedup(0.10,16))")
println("efficiency_p16_s010,$(speedup(0.10,16)/16)")
