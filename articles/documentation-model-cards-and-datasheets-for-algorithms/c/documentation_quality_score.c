#include <stdio.h>

int main(void) {
    double scores[] = {0.62, 0.6875, 0.58, 0.50, 0.56, 0.52};
    double total = 0.0;
    for (int i = 0; i < 6; i++) total += scores[i];
    printf("documentation_quality_score=%.4f\n", total / 6.0);
    return 0;
}
