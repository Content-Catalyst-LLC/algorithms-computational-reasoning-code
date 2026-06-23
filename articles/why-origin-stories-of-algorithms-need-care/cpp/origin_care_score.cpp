#include <iostream>
#include <vector>

int main() {
    std::vector<double> scores{0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98};
    double sum = 0.0;
    for (double score : scores) sum += score;
    std::cout << "origin_care_score=" << sum / scores.size() << "\n";
    return 0;
}
