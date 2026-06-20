#include <iostream>
#include <vector>
#include <utility>
#include <cmath>

std::vector<std::pair<double,double>> data() {
    return {{-2,-2.85},{-1,-0.67},{0,1.47},{1,3.63},{2,5.82}};
}

double mse(double w, double b) {
    auto rows = data();
    double total = 0.0;
    for (auto [x,y] : rows) {
        double e = y - (w*x + b);
        total += e*e;
    }
    return total / rows.size();
}

int main() {
    double w = 0.0, b = 0.0, eta = 0.08;
    auto rows = data();
    for (int step=0; step<80; ++step) {
        double grad_w = 0.0, grad_b = 0.0;
        for (auto [x,y] : rows) {
            double err = (w*x + b) - y;
            grad_w += (2.0 / rows.size()) * err * x;
            grad_b += (2.0 / rows.size()) * err;
        }
        w -= eta * grad_w;
        b -= eta * grad_b;
    }
    std::cout << "weight=" << w << " bias=" << b << " loss=" << mse(w,b) << "\n";
}
