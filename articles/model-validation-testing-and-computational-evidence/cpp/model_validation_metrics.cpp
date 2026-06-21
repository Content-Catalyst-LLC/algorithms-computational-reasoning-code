#include <cmath>
#include <iostream>
#include <vector>

int main() {
    std::vector<double> observed{33.1, 39.7, 38.8, 39.3, 8.4};
    std::vector<double> predicted{31.92, 31.58, 36.48, 25.30, 11.30};
    double squared = 0.0;
    double absolute = 0.0;
    for (std::size_t i = 0; i < observed.size(); ++i) {
        double err = observed[i] - predicted[i];
        squared += err * err;
        absolute += std::abs(err);
    }
    std::cout << "rmse=" << std::sqrt(squared / observed.size()) << "\n";
    std::cout << "mae=" << absolute / observed.size() << "\n";
    return 0;
}
