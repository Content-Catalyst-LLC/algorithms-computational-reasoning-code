#include <iostream>

unsigned long factorial(unsigned int n) {
    return n == 0 ? 1 : n * factorial(n - 1);
}

int main() {
    for (unsigned int i = 0; i <= 6; ++i) {
        std::cout << i << " " << factorial(i) << "\n";
    }
}
