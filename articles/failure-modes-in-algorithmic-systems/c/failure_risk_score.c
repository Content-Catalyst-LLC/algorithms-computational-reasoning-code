#include <stdio.h>

int main(void) {
    double likelihood = 0.42;
    double severity = 0.86;
    double detectability = 0.38;
    double controllability = 0.44;
    double failure_risk = likelihood * severity * (1.0 - detectability) * (1.0 - controllability);
    printf("failure_risk_score=%.4f\n", failure_risk);
    return 0;
}
