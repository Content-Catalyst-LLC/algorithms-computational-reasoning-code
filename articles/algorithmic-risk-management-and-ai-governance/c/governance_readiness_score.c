#include <stdio.h>

int main(void) {
    double scores[] = {0.60, 0.62, 0.58, 0.52, 0.46, 0.50};
    double total = 0.0;
    for (int i = 0; i < 6; i++) total += scores[i];
    printf("governance_readiness_score=%.4f\n", total / 6.0);
    return 0;
}
