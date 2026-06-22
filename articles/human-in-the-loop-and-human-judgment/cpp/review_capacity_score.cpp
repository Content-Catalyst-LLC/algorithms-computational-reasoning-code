#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores = {0.56, 0.62, 0.58, 0.60, 0.48};
    double total = 0.0;
    for (double score : scores) total += score;
    std::cout << "review_capacity_score=" << total / scores.size() << "\n";
    return 0;
}
