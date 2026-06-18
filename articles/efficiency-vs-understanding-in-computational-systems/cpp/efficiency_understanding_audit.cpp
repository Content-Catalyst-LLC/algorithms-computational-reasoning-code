#include <iostream>
double efficiency_gain(double baseline, double optimized){ return (baseline - optimized) / baseline; }
int main(){ std::cout << "test_name,value\nefficiency_gain_percent," << 100*efficiency_gain(100.0,64.0) << "\n"; }
