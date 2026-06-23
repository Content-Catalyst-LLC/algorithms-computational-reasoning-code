#include <stdio.h>

int main(void) {
    double total = 1200.0;
    double weights[] = {2.0, 1.0, 1.0};
    double sum = 0.0;
    for (int i = 0; i < 3; i++) sum += weights[i];
    for (int i = 0; i < 3; i++) {
        printf("share_%d=%.4f\n", i + 1, total * weights[i] / sum);
    }
    return 0;
}
