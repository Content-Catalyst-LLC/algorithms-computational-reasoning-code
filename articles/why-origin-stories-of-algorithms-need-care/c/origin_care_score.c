#include <stdio.h>

int main(void) {
    double scores[] = {0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98};
    int n = sizeof(scores) / sizeof(scores[0]);
    double sum = 0.0;
    for (int i = 0; i < n; i++) sum += scores[i];
    printf("origin_care_score=%.6f\n", sum / n);
    return 0;
}
