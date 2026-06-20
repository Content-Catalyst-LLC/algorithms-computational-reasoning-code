#include <stdio.h>

double federated_average(const double weights[], const int counts[], int n) {
    int total = 0;
    double weighted = 0.0;
    for (int i = 0; i < n; i++) {
        total += counts[i];
        weighted += weights[i] * counts[i];
    }
    return total == 0 ? 0.0 : weighted / total;
}

int main(void) {
    double weights[] = {0.42, 0.55, 0.49};
    int counts[] = {100, 240, 160};
    printf("federated average weight=%.6f\n", federated_average(weights, counts, 3));
    return 0;
}
