#include <stdio.h>

int main(void) {
    double scores[] = {0.70, 0.74, 0.62, 0.58, 0.46};
    double total = 0.0;
    for (int i = 0; i < 5; i++) total += scores[i];
    printf("explanation_quality_score=%.4f\n", total / 5.0);
    return 0;
}
