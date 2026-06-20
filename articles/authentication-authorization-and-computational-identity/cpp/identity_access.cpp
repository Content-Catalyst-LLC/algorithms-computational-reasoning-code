#include <iostream>
#include <vector>

int main() {
    std::vector<double> weights{0.10,0.11,0.11,0.09,0.09,0.10,0.09,0.09,0.08,0.06,0.06,0.02};
    double score = 0.0;
    for (double w : weights) score += 0.75 * w;
    std::cout << score * 100.0 << "\n";
    return 0;
}
