#include <iostream>
int factorial(int n){ return n <= 0 ? 1 : n * factorial(n-1); }
int main(){ std::cout << "test_name,value\nfactorial_5," << factorial(5) << "\niterative_sum," << (1+2+3) << "\n"; }
