#include <math.h>
#include <stdio.h>

double entropy(const double *p, int n) {
    double total = 0.0;
    for (int i = 0; i < n; i++) {
        if (p[i] > 0.0) total += p[i] * (log(p[i]) / log(2.0));
    }
    return -total;
}

int main(void) {
    double p[] = {0.5, 0.5};
    printf("entropy_bits=%.9f\n", entropy(p, 2));
    return 0;
}
