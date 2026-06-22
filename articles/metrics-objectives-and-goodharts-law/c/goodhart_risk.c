#include <stdio.h>

int main(void) {
    double proxy_gap = 0.38;
    double pressure = 0.88;
    double gaming = 0.72;
    double guardrail_penalty = 1.0;
    double score = (proxy_gap + pressure + gaming + guardrail_penalty) / 4.0;
    printf("goodhart_risk_score=%.4f\n", score);
    return 0;
}
