#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<double> rates = {0.42, 0.31, 0.36};
    double min_rate = *std::min_element(rates.begin(), rates.end());
    double max_rate = *std::max_element(rates.begin(), rates.end());
    std::cout << "selection_gap=" << max_rate - min_rate << "\n";
    return 0;
}
