#include <iostream>
#include <functional>

int church_apply(int n, const std::function<int(int)>& f, int x) {
    for (int i = 0; i < n; ++i) {
        x = f(x);
    }
    return x;
}

int main() {
    std::cout << "church_3_successor_0=" << church_apply(3, [](int x){ return x + 1; }, 0) << "\n";
    return 0;
}
