#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores = {0.62, 0.6875, 0.58, 0.50, 0.56, 0.52};
    double total = 0.0;
    for (double score : scores) total += score;
    std::cout << "documentation_quality_score=" << total / scores.size() << "\n";
    return 0;
}
