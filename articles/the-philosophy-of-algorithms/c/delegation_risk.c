#include <stdio.h>

double clamp(double x) { if (x < 0.0) return 0.0; if (x > 1.0) return 1.0; return x; }
int main(void) { printf("%.6f\n", clamp(0.95 * 0.95 * 0.80)); return 0; }
