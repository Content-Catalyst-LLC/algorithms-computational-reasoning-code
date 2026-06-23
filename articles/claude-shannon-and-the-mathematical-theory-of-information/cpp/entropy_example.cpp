#include <cmath>
#include <iostream>
#include <vector>

double entropy(const std::vector<double>& probs) {
    double total = 0.0;
    for (double p : probs) {
        if (p > 0.0) total += p * std::log2(p);
    }
    return -total;
}

int main() {
    std::cout << "entropy_bits=" << entropy({0.5, 0.5}) << "\n";
    return 0;
}
