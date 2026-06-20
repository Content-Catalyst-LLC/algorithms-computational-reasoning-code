scores = [0.92, 0.81, 0.77, 0.66, 0.58, 0.49, 0.42, 0.31, 0.24, 0.18]
actual = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
threshold = 0.5
predicted = [s >= threshold ? 1 : 0 for s in scores]
tp = sum((predicted .== 1) .& (actual .== 1))
fp = sum((predicted .== 1) .& (actual .== 0))
tn = sum((predicted .== 0) .& (actual .== 0))
fn = sum((predicted .== 0) .& (actual .== 1))
println((TP=tp, FP=fp, TN=tn, FN=fn))
