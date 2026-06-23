#include <stdio.h>

int main(void) {
    double pd = 0.035;
    double lgd = 0.45;
    double ead = 100000.0;
    double expected_loss = pd * lgd * ead;
    printf("expected_loss=%.4f\n", expected_loss);
    return 0;
}
