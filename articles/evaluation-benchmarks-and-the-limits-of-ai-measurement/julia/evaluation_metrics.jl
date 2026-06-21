tp, tn, fp, fn = 42, 38, 7, 13
accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
println("accuracy=", round(accuracy, digits=4))
println("f1=", round(f1, digits=4))
