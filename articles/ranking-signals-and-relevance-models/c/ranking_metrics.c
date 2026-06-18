#include <stdio.h>
double precision_at_k(double tp,double k){ return k == 0 ? 0 : tp/k; }
double ranking_score(double l,double m,double f,double a,double s,double p){ return 100*(0.22*l+0.18*m+0.12*f+0.16*a+0.17*s+0.15*p); }
int main(void){ printf("test_name,value\nprecision_at_3,%.4f\nranking_signal_score,%.3f\n", precision_at_k(2,3), ranking_score(.84,.88,.76,.82,.78,.86)); return 0; }
