#include <stdio.h>

int main(void) {
    double scores[] = {0.94, 0.78, 0.56, 0.70};
    double total = 0.0;
    for (int i = 0; i < 4; i++) total += scores[i];
    printf("non_use_pressure_score=%.4f\n", total / 4.0);
    return 0;
}
