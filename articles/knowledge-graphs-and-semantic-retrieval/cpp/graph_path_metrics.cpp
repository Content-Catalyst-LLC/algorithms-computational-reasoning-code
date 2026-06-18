#include <iostream>
#include <algorithm>
double hybrid_score(double l,double v,double g,double p){ return 100*(0.25*l+0.25*v+0.25*g+0.25*p); }
double path_score(double path_length,double confidence,double provenance,double review){
  double length_factor = 1.0/(1.0+std::max(path_length-1.0,0.0));
  return 100*(0.25*length_factor+0.30*confidence+0.30*provenance+0.15*review);
}
int main(){ std::cout << "test_name,value\nhybrid_score," << hybrid_score(.82,.78,.88,.90) << "\ngraph_path_score," << path_score(3,.90,.92,.95) << "\n"; }
