#include <iostream>
#include <iomanip>
int main() { double post_alpha=2.0+113.0, post_beta=2.0+72.0; std::cout << std::fixed << std::setprecision(6) << "posterior_mean=" << post_alpha/(post_alpha+post_beta) << "\n"; return 0; }
