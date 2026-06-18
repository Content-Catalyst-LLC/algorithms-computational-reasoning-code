#include <iostream>
#include <cmath>
double freshness(double days,double decay){ return std::exp(-decay*days); }
double quality(double v,double f,double c,double l,double m){ return 100*(0.25*v+0.18*f+0.20*c+0.22*l+0.15*m); }
int main(){ std::cout << "test_name,value\nfreshness_3_days," << freshness(3,0.025) << "\npipeline_quality_score," << quality(.92,.86,.90,.88,.82) << "\n"; }
