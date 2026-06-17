#include <iostream>
#include <vector>
bool nondecreasing(const std::vector<int>& xs){ for(size_t i=0;i+1<xs.size();++i){ if(xs[i] > xs[i+1]) return false; } return true; }
int main(){ std::cout << "test_name,status\nsorted_valid," << (nondecreasing({1,2,2,3})?"pass":"fail") << "\nsorted_invalid," << (nondecreasing({1,3,2})?"pass":"fail") << "\n"; }
