#include <iostream>
#include <cmath>

int main() {
    int digit = 7;
    int base = 10;
    int position = 3;
    int value = digit * static_cast<int>(std::pow(base, position));
    std::cout << "place_value=" << value << "\n";
    return 0;
}
