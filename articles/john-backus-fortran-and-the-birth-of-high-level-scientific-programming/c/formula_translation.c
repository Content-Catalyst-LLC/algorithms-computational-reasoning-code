#include <stdio.h>

double formula(double x, double a, double b, double c) {
    return a*x*x + b*x + c;
}

int main(void) {
    double xs[] = {-2, -1, 0, 1, 2, 3};
    for (int i = 0; i < 6; ++i) {
        printf("x=%.1f, y=%.6f\n", xs[i], formula(xs[i], 2.0, -3.0, 1.0));
    }
    return 0;
}
