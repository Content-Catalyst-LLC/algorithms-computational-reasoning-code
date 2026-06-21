#include <math.h>
#include <stdio.h>

double sigmoid(double x) { return 1.0 / (1.0 + exp(-x)); }
double representation_score(double x1, double x2, double x3, double bias) {
    return sigmoid(0.9*x1 - 0.7*x2 + 0.35*x3 + bias);
}
int main(void) {
    printf("%.6f\n", representation_score(0.5, -0.2, 0.7, 0.0));
    return 0;
}
