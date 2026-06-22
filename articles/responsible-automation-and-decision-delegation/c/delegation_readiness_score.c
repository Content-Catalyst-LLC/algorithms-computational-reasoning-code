#include <stdio.h>

int main(void) {
    double scores[] = {0.62, 0.58, 0.46, 0.52, 0.60, 0.58};
    double total = 0.0;
    for (int i = 0; i < 6; i++) total += scores[i];
    printf("delegation_readiness_score=%.4f\n", total / 6.0);
    return 0;
}
