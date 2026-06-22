#include <stdio.h>

int main(void) {
    double current_stock = 100.0;
    double inflow = 12.0;
    double outflow = 7.0;
    double next_stock = current_stock + inflow - outflow;
    printf("next_stock=%.4f\n", next_stock);
    return 0;
}
