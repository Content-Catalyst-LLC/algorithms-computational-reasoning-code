function rates(tp, fp, tn, fn)
    total = max(1, tp + fp + tn + fn)
    accuracy = (tp + tn) / total
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    return accuracy, precision, recall
end

accuracy, precision, recall = rates(80, 25, 140, 35)
println("accuracy=$(round(accuracy, digits=6))")
println("precision=$(round(precision, digits=6))")
println("recall=$(round(recall, digits=6))")
