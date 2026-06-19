#include <stdio.h>
unsigned long long branching_state_count(unsigned long long b, int d){ unsigned long long total=0, pow=1; for(int i=0;i<=d;i++){ if(i==0) pow=1; else pow*=b; total+=pow; } return total; }
double ratio(double n,double d){ return d == 0 ? 0 : n/d; }
int main(void){ printf("test_name,value\nbranching_state_count,%llu\npath_cost,%.3f\nheuristic_score,%.3f\ncoverage_ratio,%.6f\npruning_ratio,%.6f\n", branching_state_count(3,5), 11.5, 13.5, ratio(850,5000), ratio(1200,4200)); return 0; }
