#include <stdio.h>

int main(void) {
    double value = 12.0;
    double trigger = 10.0;
    printf("event_triggered=%s\n", value >= trigger ? "true" : "false");
    return 0;
}
