#include <stdio.h>

int main(void) {
    double tp = 42, tn = 38, fp = 7, fn = 13;
    double accuracy = (tp + tn) / (tp + tn + fp + fn);
    printf("accuracy=%.4f\n", accuracy);
    return 0;
}
