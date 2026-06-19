edge_response_time(sense, filter, compute, actuate) = sense + filter + compute + actuate
cloud_response_time(sense, uplink, cloud_compute, downlink, actuate) = sense + uplink + cloud_compute + downlink + actuate
battery_life_hours(battery_wh, average_power_w) = average_power_w == 0 ? 0 : battery_wh / average_power_w
local_action(signal, threshold) = signal >= threshold ? "alert" : "monitor"
println("test_name,value")
println("edge_response_time_ms,$(edge_response_time(8,6,14,5))")
println("cloud_response_time_ms,$(cloud_response_time(8,90,60,90,5))")
println("battery_life_hours,$(battery_life_hours(12,0.08))")
println("local_action,$(local_action(0.82,0.75))")
