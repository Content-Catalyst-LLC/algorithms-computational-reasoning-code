#include <iostream>
double precision(double tp,double retrieved){ return retrieved == 0 ? 0 : tp/retrieved; }
double recall(double tp,double relevant){ return relevant == 0 ? 0 : tp/relevant; }
int main(){ std::cout << "test_name,value\nprecision," << precision(2,3) << "\nrecall," << recall(2,2) << "\n"; }
