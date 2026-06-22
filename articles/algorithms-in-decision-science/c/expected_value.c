#include <stdio.h>

int main(void) {
    double probability = 0.82;
    double benefit_if_act = 0.88;
    double cost_if_act = 0.30;
    double expected_value = probability * benefit_if_act - cost_if_act;
    printf("expected_value_of_action=%.4f\n", expected_value);
    return 0;
}
