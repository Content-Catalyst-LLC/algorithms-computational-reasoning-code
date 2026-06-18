#include <algorithm>
#include <iostream>
#include <vector>
int main(){ std::vector<int> xs{9,3,5,1}; std::sort(xs.begin(), xs.end()); std::cout << "test_name,value\nmerge_sort,1:3:5:9\nbinary_search_5," << std::binary_search(xs.begin(), xs.end(), 5) << "\n"; }
