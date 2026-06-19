#include <iostream>
double dependency_score(double a,double v,double c,double s,double e){ return 100.0*(0.22*a+0.22*v+0.18*c+0.24*s+0.14*e); }
double switching_cost(double m,double r,double t,double d,double l){ return m+r+t+d+l; }
double ratio(double n,double d){ return d == 0 ? 0 : n/d; }
int main(){ std::cout << "test_name,value\ndependency_score," << dependency_score(.80,.90,.70,.85,.65) << "\nswitching_cost," << switching_cost(45000,120000,18000,24000,75000) << "\napi_dependency_ratio," << ratio(850000,1000000) << "\nvisibility_share," << ratio(250000,5000000) << "\n"; }
