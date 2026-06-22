#include <stdio.h>

int main(void) {
    double scores[] = {0.72, 0.68, 0.64, 0.58, 0.52, 0.66};
    double total = 0.0;
    for (int i = 0; i < 6; i++) total += scores[i];
    printf("accountability_capacity_score=%.4f\n", total / 6.0);
    return 0;
}
