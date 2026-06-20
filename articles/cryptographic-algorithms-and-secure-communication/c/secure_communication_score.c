#include <stdio.h>

double score(double threat_model, double keys, double validation, double integrity, double authentication) {
    return 100.0 * (0.22 * threat_model + 0.24 * keys + 0.18 * validation + 0.18 * integrity + 0.18 * authentication);
}

int main(void) {
    printf("standard secure channel score=%.2f\n", score(0.86, 0.82, 0.90, 0.86, 0.84));
    printf("legacy manual transfer score=%.2f\n", score(0.36, 0.24, 0.18, 0.34, 0.28));
    return 0;
}
