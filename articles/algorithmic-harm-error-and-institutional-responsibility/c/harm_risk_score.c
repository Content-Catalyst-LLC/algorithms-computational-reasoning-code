#include <stdio.h>

int main(void) {
    double error_likelihood = 0.34;
    double severity = 0.92;
    double exposure = 0.78;
    double contestability = 0.42;
    double harm_risk = error_likelihood * severity * exposure * (1.0 - contestability);
    printf("harm_risk_score=%.4f\n", harm_risk);
    return 0;
}
