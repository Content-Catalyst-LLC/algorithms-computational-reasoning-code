#include <iostream>
#include <vector>

int threshold_unit(const std::vector<int>& inputs, const std::vector<int>& weights, int threshold) {
    int total = 0;
    for (size_t i = 0; i < inputs.size(); ++i) total += inputs[i] * weights[i];
    return total >= threshold ? 1 : 0;
}

int main() {
    std::cout << threshold_unit({1, 1}, {1, 1}, 2) << "\n";
}
