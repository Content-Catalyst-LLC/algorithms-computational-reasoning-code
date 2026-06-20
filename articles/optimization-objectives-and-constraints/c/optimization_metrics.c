#include <stdio.h>
double linear_objective(double c[], double x[], int n){ double total=0; for(int i=0;i<n;i++) total += c[i]*x[i]; return total; }
double constraint_margin(double limit, double observed){ return limit - observed; }
double penalty_objective(double base, double penalty, double weight){ return base + weight * penalty; }
double tradeoff(double cost, double quality, double risk){ return 0.35*(1-cost) + 0.40*quality + 0.25*(1-risk); }
int main(void){ double c[]={4.0,2.0,1.5}; double x[]={10.0,20.0,5.0}; printf("test_name,value\nlinear_objective,%.3f\nconstraint_margin,%.3f\npenalty_objective,%.3f\nnormalized_tradeoff_score,%.6f\n", linear_objective(c,x,3), constraint_margin(100.0,86.5), penalty_objective(42.0,8.0,2.5), tradeoff(0.30,0.82,0.25)); return 0; }
