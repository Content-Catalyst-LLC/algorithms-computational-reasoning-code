#include <stdio.h>

int threshold_unit(const int inputs[], const int weights[], int n, int threshold) {
    int total = 0;
    for (int i = 0; i < n; ++i) total += inputs[i] * weights[i];
    return total >= threshold ? 1 : 0;
}

int main(void) {
    int inputs[] = {1, 1};
    int weights[] = {1, 1};
    printf("%d\n", threshold_unit(inputs, weights, 2, 2));
    return 0;
}
