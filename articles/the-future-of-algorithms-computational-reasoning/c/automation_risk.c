#include <stdio.h>

double clamp(double x) {
    if (x < 0.0) return 0.0;
    if (x > 1.0) return 1.0;
    return x;
}

int main(void) {
    double risk = clamp(0.95 * 0.85 * 0.90 * 0.80);
    printf("%.6f\n", risk);
    return 0;
}
