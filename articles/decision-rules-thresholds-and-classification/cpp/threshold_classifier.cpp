#include <iostream>

int classify(double score, double threshold) {
    return score >= threshold ? 1 : 0;
}

int main() {
    std::cout << classify(0.72, 0.50) << std::endl;
    return 0;
}
