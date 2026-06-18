#include <iostream>
double missingness_rate(double missing,double total){ return total == 0 ? 0 : missing/total; }
double quality(double c,double v,double t,double p,double val){ return 100*(0.25*c+0.20*v+0.15*t+0.22*p+0.18*val); }
int main(){ double mr=missingness_rate(45,1000); std::cout << "test_name,value\nmissingness_rate_45_of_1000," << mr << "\ncompleteness_score_45_of_1000," << 1-mr << "\ndata_quality_score," << quality(.92,.88,.86,.90,.89) << "\n"; }
