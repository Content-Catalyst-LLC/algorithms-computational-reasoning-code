#include <iostream>
bool score_in_range(double x){ return x >= 0.0 && x <= 100.0; }
int main(){ std::cout << "test_name,status\nscore_72," << (score_in_range(72)?"pass":"fail") << "\nscore_150," << (score_in_range(150)?"pass":"fail") << "\n"; }
