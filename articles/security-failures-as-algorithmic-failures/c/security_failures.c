#include <stdio.h>

int main(void) {
    double weights[] = {0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03};
    int n = sizeof(weights) / sizeof(weights[0]);
    double score = 0.0;
    for (int i = 0; i < n; ++i) score += weights[i] * 0.65;
    printf("%.3f\n", score * 100.0);
    return 0;
}
