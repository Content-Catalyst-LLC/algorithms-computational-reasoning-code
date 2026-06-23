#include <stdio.h>

int main(void) {
    double b = 10.0;
    double c = 39.0;
    double completion = (b / 2.0) * (b / 2.0);
    printf("completion_term=%.6f\n", completion);
    printf("completed_rhs=%.6f\n", c + completion);
    return 0;
}
