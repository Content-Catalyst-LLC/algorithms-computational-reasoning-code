#include <stdio.h>

int main(void) {
    double provenance_risk = 0.66;
    double measurement_weakness = 0.58;
    double proxy_risk = 0.62;
    double remediation = 0.42;
    double score = (provenance_risk + measurement_weakness + proxy_risk + (1.0 - remediation)) / 4.0;
    printf("historical_risk_score=%.4f\n", score);
    return 0;
}
