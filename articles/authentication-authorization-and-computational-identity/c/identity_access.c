#include <stdio.h>

int main(void) {
    double weights[] = {0.10,0.11,0.11,0.09,0.09,0.10,0.09,0.09,0.08,0.06,0.06,0.02};
    double score = 0.0;
    for (int i = 0; i < 12; ++i) score += 0.75 * weights[i];
    printf("%.3f\n", score * 100.0);
    return 0;
}
