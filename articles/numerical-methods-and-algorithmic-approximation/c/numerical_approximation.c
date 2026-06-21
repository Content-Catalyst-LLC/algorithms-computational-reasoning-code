#include <math.h>
#include <stdio.h>

double f(double x) { return sin(x) + 0.25 * x * x; }
double central_difference(double x, double h) { return (f(x + h) - f(x - h)) / (2.0 * h); }
int main(void) { printf("%.12f\n", central_difference(1.0, 0.01)); return 0; }
