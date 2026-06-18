#include <iostream>
double speedup(double s, double p){ return 1.0 / (s + ((1.0-s)/p)); }
int main(){ double sp=speedup(0.10,16.0); std::cout << "test_name,value\nspeedup_p16_s010," << sp << "\nefficiency_p16_s010," << sp/16.0 << "\n"; }
