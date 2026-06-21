#include <stdio.h>

int main(void) {
    double tp = 80.0, fp = 25.0, tn = 140.0, fn = 35.0;
    double total = tp + fp + tn + fn;
    printf("accuracy=%.6f\n", (tp + tn) / total);
    printf("precision=%.6f\n", tp / (tp + fp));
    printf("recall=%.6f\n", tp / (tp + fn));
    return 0;
}
