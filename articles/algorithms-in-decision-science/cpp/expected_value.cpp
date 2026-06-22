#include <iostream>

int main() {
    double probability = 0.82;
    double benefit_if_act = 0.88;
    double cost_if_act = 0.30;
    double expected_value = probability * benefit_if_act - cost_if_act;
    std::cout << "expected_value_of_action=" << expected_value << "\n";
    return 0;
}
