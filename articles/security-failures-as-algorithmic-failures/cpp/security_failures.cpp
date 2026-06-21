#include <iostream>
#include <vector>
#include <iomanip>

int main() {
    std::vector<double> weights{0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03};
    double score = 0.0;
    for (double w : weights) score += w * 0.65;
    std::cout << std::fixed << std::setprecision(3) << score * 100.0 << "\n";
    return 0;
}
