#include <stdio.h>

int main(void) {
    double level = 7.5;
    double threshold = 5.0;
    printf("action_triggered=%s\n", level >= threshold ? "true" : "false");
    return 0;
}
