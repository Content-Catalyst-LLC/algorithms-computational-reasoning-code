#include <stdio.h>

const char* decision(double score, double threshold) {
    return score >= threshold ? "act" : "monitor";
}

int main(void) {
    double baseline = 0.42;
    double intervention = 0.57;
    printf("estimated_effect=%.6f
", intervention - baseline);
    printf("baseline_decision=%s
", decision(0.53, 0.55));
    printf("new_threshold_decision=%s
", decision(0.53, 0.50));
    return 0;
}
