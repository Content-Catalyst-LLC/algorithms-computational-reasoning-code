#include <iostream>
#include <vector>
double linear_objective(const std::vector<double>& c,const std::vector<double>& x){ double total=0; for(size_t i=0;i<c.size();++i) total += c[i]*x[i]; return total; }
double constraint_margin(double limit,double observed){ return limit-observed; }
double penalty_objective(double base,double penalty,double weight){ return base + weight*penalty; }
double tradeoff(double cost,double quality,double risk){ return 0.35*(1-cost) + 0.40*quality + 0.25*(1-risk); }
int main(){ std::cout << "test_name,value\nlinear_objective," << linear_objective({4.0,2.0,1.5},{10.0,20.0,5.0}) << "\nconstraint_margin," << constraint_margin(100.0,86.5) << "\npenalty_objective," << penalty_objective(42.0,8.0,2.5) << "\nnormalized_tradeoff_score," << tradeoff(0.30,0.82,0.25) << "\n"; }
