#include <iostream>
#include <iomanip>

int main() {
    double x0 = 10.0, y0 = 1.2;
    double x1 = 20.0, y1 = 2.8;
    double x = 15.0;
    double y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0);
    std::cout << std::fixed << std::setprecision(6) << "interpolated_y=" << y << "\n";
    return 0;
}
