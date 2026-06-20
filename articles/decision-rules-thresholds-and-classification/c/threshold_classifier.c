#include <stdio.h>

int classify(double score, double threshold) {
    return score >= threshold ? 1 : 0;
}

int main(void) {
    printf("%d\n", classify(0.72, 0.50));
    return 0;
}
