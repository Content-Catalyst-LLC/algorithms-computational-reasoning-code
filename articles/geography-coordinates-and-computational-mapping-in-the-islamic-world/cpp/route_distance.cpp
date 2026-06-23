#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<double> segments = {12.0, 20.0, 7.5};
    double total = std::accumulate(segments.begin(), segments.end(), 0.0);
    std::cout << "segments=" << segments.size() << "\n";
    std::cout << "total_distance=" << total << "\n";
    return 0;
}
