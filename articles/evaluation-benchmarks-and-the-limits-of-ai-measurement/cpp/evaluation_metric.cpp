#include <iostream>

int main() {
    double tp = 42, tn = 38, fp = 7, fn = 13;
    double accuracy = (tp + tn) / (tp + tn + fp + fn);
    std::cout << "accuracy=" << accuracy << "\n";
    return 0;
}
