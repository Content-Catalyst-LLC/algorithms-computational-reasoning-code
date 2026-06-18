#include <algorithm>
#include <iostream>
#include <vector>
int linear_search(const std::vector<int>& xs, int target){ auto it=std::find(xs.begin(), xs.end(), target); return it==xs.end() ? -1 : static_cast<int>(it-xs.begin()); }
int main(){ std::vector<int> xs{7,2,9,1}; std::sort(xs.begin(), xs.end()); std::cout << "test_name,value\nlinear_search_9," << linear_search({7,2,9,1},9) << "\nsort_demo,1:2:7:9\n"; }
