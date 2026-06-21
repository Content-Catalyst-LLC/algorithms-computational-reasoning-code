#include <math.h>
#include <stdio.h>

int main(void) {
    double observed[] = {33.1, 39.7, 38.8, 39.3, 8.4};
    double predicted[] = {31.92, 31.58, 36.48, 25.30, 11.30};
    int n = 5;
    double squared = 0.0;
    double absolute = 0.0;
    for (int i = 0; i < n; i++) {
        double err = observed[i] - predicted[i];
        squared += err * err;
        absolute += fabs(err);
    }
    printf("rmse=%.4f\n", sqrt(squared / n));
    printf("mae=%.4f\n", absolute / n);
    return 0;
}
