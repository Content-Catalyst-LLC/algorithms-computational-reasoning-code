#include <stdio.h>

const char* label(double score, double threshold) {
    return score >= threshold ? "favorable" : "not_favorable";
}

int main(void) {
    double original = 0.57;
    double counterfactual = 0.65;
    double threshold = 0.62;
    printf("original_label=%s\n", label(original, threshold));
    printf("counterfactual_label=%s\n", label(counterfactual, threshold));
    printf("decision_flipped=%s\n", original < threshold && counterfactual >= threshold ? "true" : "false");
    return 0;
}
