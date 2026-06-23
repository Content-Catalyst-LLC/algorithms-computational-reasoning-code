#include <stdio.h>

int main(void) {
    double hazard = 0.80;
    double exposure = 0.75;
    double vulnerability = 0.60;
    double risk = hazard * exposure * vulnerability;
    printf("infrastructure_risk=%.4f\n", risk);
    return 0;
}
