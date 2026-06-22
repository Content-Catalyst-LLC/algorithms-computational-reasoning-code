#include <iostream>

int main() {
    double current_stock = 100.0;
    double inflow = 12.0;
    double outflow = 7.0;
    double next_stock = current_stock + inflow - outflow;
    std::cout << "next_stock=" << next_stock << "\n";
    return 0;
}
