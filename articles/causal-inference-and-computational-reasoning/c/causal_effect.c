#include <stdio.h>

double effect(double treated_mean, double control_mean) {
    return treated_mean - control_mean;
}

int main(void) {
    printf("causal contrast = %.4f\n", effect(0.64, 0.47));
    return 0;
}
