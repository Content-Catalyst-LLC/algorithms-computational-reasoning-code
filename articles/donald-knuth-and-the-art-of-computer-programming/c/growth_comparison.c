#include <math.h>
#include <stdio.h>

int main(void) {
    double n = 1000.0;
    printf("log2_n=%.6f\n", log2(n));
    printf("n=%.0f\n", n);
    printf("n_log2_n=%.6f\n", n * log2(n));
    printf("n_squared=%.0f\n", n * n);
    return 0;
}
