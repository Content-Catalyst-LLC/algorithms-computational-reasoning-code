#include <iostream>

int main() {
    double b = 10.0;
    double c = 39.0;
    double completion = (b / 2.0) * (b / 2.0);
    std::cout << "completion_term=" << completion << "\n";
    std::cout << "completed_rhs=" << c + completion << "\n";
    return 0;
}
