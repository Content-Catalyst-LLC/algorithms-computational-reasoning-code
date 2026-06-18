#include <iostream>
int growth(int b, int d){ int total=0, pow=1; for(int i=0;i<=d;i++){ total += pow; pow *= b; } return total; }
int main(){ std::cout << "test_name,value\nsearch_space_growth," << growth(2,3) << "\npermutation_count,6\n"; }
