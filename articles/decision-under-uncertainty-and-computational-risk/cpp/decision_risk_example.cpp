#include <algorithm>
#include <iostream>

double expected_net_value(double p, double benefit, double loss, double cost) {
    p = std::clamp(p, 0.0, 1.0);
    return p * benefit - p * loss - cost;
}

int main() {
    std::cout << expected_net_value(0.42, 150.0, 80.0, 25.0) << "
";
}
