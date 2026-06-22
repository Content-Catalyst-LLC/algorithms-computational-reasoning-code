#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores = {0.70, 0.74, 0.62, 0.58, 0.46};
    double total = 0.0;
    for (double score : scores) total += score;
    std::cout << "explanation_quality_score=" << total / scores.size() << "\n";
    return 0;
}
