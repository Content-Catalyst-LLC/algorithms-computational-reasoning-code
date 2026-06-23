#include <stdio.h>

int main(void) {
    double tp = 86.0;
    double fn = 14.0;
    double sensitivity = tp / (tp + fn);
    printf("sensitivity=%.4f\n", sensitivity);
    return 0;
}
