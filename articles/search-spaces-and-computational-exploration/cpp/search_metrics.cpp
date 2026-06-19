#include <iostream>
unsigned long long branching_state_count(unsigned long long b, int d){ unsigned long long total=0, pow=1; for(int i=0;i<=d;i++){ if(i==0) pow=1; else pow*=b; total+=pow; } return total; }
double ratio(double n,double d){ return d == 0 ? 0 : n/d; }
int main(){ std::cout << "test_name,value\nbranching_state_count," << branching_state_count(3,5) << "\npath_cost," << 11.5 << "\nheuristic_score," << 13.5 << "\ncoverage_ratio," << ratio(850,5000) << "\npruning_ratio," << ratio(1200,4200) << "\n"; }
