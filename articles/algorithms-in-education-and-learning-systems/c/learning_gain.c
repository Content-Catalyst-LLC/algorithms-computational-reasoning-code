#include <stdio.h>

int main(void) {
    double pretest = 0.52;
    double posttest = 0.78;
    double gain = posttest - pretest;
    printf("learning_gain=%.4f\n", gain);
    return 0;
}
