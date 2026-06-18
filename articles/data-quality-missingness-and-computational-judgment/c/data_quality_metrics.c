#include <stdio.h>
double missingness_rate(double missing,double total){ return total == 0 ? 0 : missing/total; }
double quality(double c,double v,double t,double p,double val){ return 100*(0.25*c+0.20*v+0.15*t+0.22*p+0.18*val); }
int main(void){ double mr=missingness_rate(45,1000); printf("test_name,value\nmissingness_rate_45_of_1000,%.4f\ncompleteness_score_45_of_1000,%.4f\ndata_quality_score,%.3f\n", mr, 1-mr, quality(.92,.88,.86,.90,.89)); return 0; }
