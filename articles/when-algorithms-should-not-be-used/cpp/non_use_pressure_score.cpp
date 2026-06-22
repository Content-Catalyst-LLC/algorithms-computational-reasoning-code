#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores = {0.94, 0.78, 0.56, 0.70};
    double total = 0.0;
    for (double score : scores) total += score;
    std::cout << "non_use_pressure_score=" << total / scores.size() << "\n";
    return 0;
}
