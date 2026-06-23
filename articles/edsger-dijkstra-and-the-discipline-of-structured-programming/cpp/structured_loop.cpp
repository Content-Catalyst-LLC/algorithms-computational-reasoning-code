#include <iostream>

int sum_to(int n) {
    int acc = 0;
    for (int i = 0; i <= n; ++i) {
        acc += i;
    }
    return acc;
}

int main() {
    std::cout << "sum_to_5=" << sum_to(5) << "\n";
}
