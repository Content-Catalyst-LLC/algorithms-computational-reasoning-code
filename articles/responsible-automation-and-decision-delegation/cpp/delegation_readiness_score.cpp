#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores = {0.62, 0.58, 0.46, 0.52, 0.60, 0.58};
    double total = 0.0;
    for (double score : scores) total += score;
    std::cout << "delegation_readiness_score=" << total / scores.size() << "\n";
    return 0;
}
