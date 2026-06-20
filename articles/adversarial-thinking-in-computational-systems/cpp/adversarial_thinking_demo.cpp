#include <iostream>
#include <vector>
#include <numeric>

struct SurfaceRisk {
    double exposure;
    double control;
};

double residual_surface_risk(const SurfaceRisk& risk) {
    return risk.exposure * (1.0 - risk.control);
}

int main() {
    std::vector<SurfaceRisk> risks = {{0.75, 0.62}, {0.68, 0.55}, {0.52, 0.70}};
    double total = 0.0;
    for (const auto& risk : risks) {
        total += residual_surface_risk(risk);
    }
    std::cout << "average residual surface risk=" << total / risks.size() << "\n";
    return 0;
}
