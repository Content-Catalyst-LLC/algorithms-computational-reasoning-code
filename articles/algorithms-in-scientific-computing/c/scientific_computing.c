#include <math.h>
#include <stdio.h>

double f(double x) { return sin(x); }
double central_difference(double x, double h) { return (f(x + h) - f(x - h)) / (2.0 * h); }
double trapezoid(int n) {
    double a = 0.0, b = M_PI, h = (b - a) / n;
    double total = 0.5 * (f(a) + f(b));
    for (int i = 1; i < n; ++i) total += f(a + i * h);
    return h * total;
}
int main(void) {
    printf("central_difference=%.12f\n", central_difference(1.0, 1e-4));
    printf("trapezoid_integral=%.12f\n", trapezoid(200));
    return 0;
}
