#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores = {0.72, 0.68, 0.64, 0.58, 0.52, 0.66};
    double total = 0.0;
    for (double score : scores) total += score;
    std::cout << "accountability_capacity_score=" << total / scores.size() << "\n";
    return 0;
}
