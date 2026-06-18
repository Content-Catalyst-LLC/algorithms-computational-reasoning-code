#include <iostream>
double speedup(double t1,double tp){ return tp == 0 ? 0 : t1/tp; }
double amdahl(double p,double s){ return p == 0 ? 0 : 1.0/(s+((1.0-s)/p)); }
double efficiency(double p,double sp){ return p == 0 ? 0 : sp/p; }
int main(){ double sp=speedup(120,28); std::cout << "test_name,value\nobserved_speedup_120_to_28," << sp << "\namdahl_speedup_8_workers," << amdahl(8,0.12) << "\nefficiency_8_workers," << efficiency(8,sp) << "\n"; }
