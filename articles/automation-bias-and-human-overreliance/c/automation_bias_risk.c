#include <stdio.h>

int main(void) {
    double acceptance = 0.93;
    double quality = 0.71;
    double uncertainty = 0.29;
    double review_deficit = 0.65;
    double override_friction = 0.72;
    double weak_contestability = 0.0;
    double overreliance_gap = acceptance - quality;
    if (overreliance_gap < 0) overreliance_gap = 0;
    double score = (acceptance + overreliance_gap + uncertainty + review_deficit + override_friction + weak_contestability) / 6.0;
    printf("automation_bias_risk_score=%.4f\n", score);
    return 0;
}
