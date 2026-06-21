#include <stdio.h>
double rate(double num, double den) { return den == 0.0 ? 0.0 : num / den; }
int main(void) { printf("false_positive_rate=%.4f\n", rate(18, 106)); return 0; }
