#include <math.h>
#include <stdio.h>

double standard_error(double p_hat, double n) {
    return sqrt((p_hat * (1.0 - p_hat)) / n);
}

int main(void) {
    double p_hat = 0.57;
    double n = 1000.0;
    printf("p_hat=%.3f standard_error=%.6f\n", p_hat, standard_error(p_hat, n));
    return 0;
}
