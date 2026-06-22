#include <stdio.h>

int main(void) {
    double rates[] = {0.42, 0.31, 0.36};
    double min_rate = rates[0];
    double max_rate = rates[0];
    for (int i = 0; i < 3; i++) {
        if (rates[i] < min_rate) min_rate = rates[i];
        if (rates[i] > max_rate) max_rate = rates[i];
    }
    printf("selection_gap=%.4f\n", max_rate - min_rate);
    return 0;
}
