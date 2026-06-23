#include <iostream>

int main() {
    double pretest = 0.52;
    double posttest = 0.78;
    double gain = posttest - pretest;
    std::cout << "learning_gain=" << gain << "\n";
    return 0;
}
