#include <stdio.h>

int main(void) {
    double scores[] = {0.56, 0.62, 0.58, 0.60, 0.48};
    double total = 0.0;
    for (int i = 0; i < 5; i++) total += scores[i];
    printf("review_capacity_score=%.4f\n", total / 5.0);
    return 0;
}
