#include <iostream>
#include <vector>
#include <numeric>

int main() {
    double total = 1200.0;
    std::vector<double> weights = {2.0, 1.0, 1.0};
    double sum = std::accumulate(weights.begin(), weights.end(), 0.0);
    for (std::size_t i = 0; i < weights.size(); ++i) {
        std::cout << "share_" << i + 1 << "=" << total * weights[i] / sum << "\n";
    }
    return 0;
}
