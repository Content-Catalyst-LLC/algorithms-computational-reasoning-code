#include <stdio.h>

int main(void) {
    double amplification = 0.82;
    double concentration = 0.76;
    double intervention = 0.44;
    double drift = 0.28;
    double recursive_data = 0.31;
    double score = (amplification + concentration + intervention + drift + recursive_data) / 5.0;
    printf("feedback_risk_score=%.4f\n", score);
    return 0;
}
