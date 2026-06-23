#include <stdio.h>
#include <math.h>

int main(void) {
    double ns[] = {10, 100, 1000, 10000};
    for (int i = 0; i < 4; ++i) {
        double n = ns[i];
        printf("n=%.0f, log2=%.6f, nlogn=%.6f, n2=%.0f\n", n, log2(n), n*log2(n), n*n);
    }
    return 0;
}
