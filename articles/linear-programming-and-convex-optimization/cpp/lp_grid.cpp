#include <iostream>
#include <tuple>

bool feasible(int x, int y) {
    return 2*x + y <= 8 && x + 2*y <= 8 && x >= 0 && y >= 0;
}

int objective(int x, int y) { return 3*x + 4*y; }

int main() {
    std::tuple<int,int,int> best{0,0,-1};
    for (int x=0; x<10; ++x) {
        for (int y=0; y<10; ++y) {
            if (feasible(x,y) && objective(x,y) > std::get<2>(best)) {
                best = {x,y,objective(x,y)};
            }
        }
    }
    std::cout << "best x=" << std::get<0>(best) << " y=" << std::get<1>(best) << " objective=" << std::get<2>(best) << "\n";
}
