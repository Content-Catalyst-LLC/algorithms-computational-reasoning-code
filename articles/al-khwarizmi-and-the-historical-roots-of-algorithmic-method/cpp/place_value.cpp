#include <iostream>
#include <vector>

int main() {
    std::vector<int> digits{1, 2, 3, 0};
    int value = 0;
    for (int digit : digits) {
        value = value * 10 + digit;
    }
    std::cout << "place_value_result=" << value << "\n";
    return 0;
}
