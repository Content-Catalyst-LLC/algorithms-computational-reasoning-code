#include <iostream>
double query_score(double e,double r,double p,double j,double k,double m){ return 100*(0.18*e+0.18*r+0.18*p+0.18*j+0.14*k+0.14*m); }
int main(){ std::cout << "test_name,value\nquery_logic_core_score," << query_score(.88,.86,.84,.82,.84,.80) << "\n"; }
