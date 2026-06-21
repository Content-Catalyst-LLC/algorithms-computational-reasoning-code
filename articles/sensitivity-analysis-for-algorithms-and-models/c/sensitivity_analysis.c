#include <stdio.h>

double clamp(double x) { return x < 0 ? 0 : (x > 1 ? 1 : x); }
double model(double demand, double capacity, double failure, double adaptation) {
    return clamp(0.5 + 0.30*demand + 0.25*failure - 0.20*capacity - 0.15*adaptation);
}
int main(void) {
    printf("baseline_risk=%.6f\n", model(0.45, 0.35, 0.25, 0.30));
    return 0;
}
