#include <iostream>

int main() {
    double pace = 0.84;
    double hours = 0.72;
    double fatigue = 0.70;
    double schedule_volatility = 0.78;
    double burden = (pace + hours + fatigue + schedule_volatility) / 4.0;
    std::cout << "workload_burden_score=" << burden << "\n";
    return 0;
}
