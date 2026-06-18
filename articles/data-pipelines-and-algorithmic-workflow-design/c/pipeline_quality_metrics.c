#include <stdio.h>
#include <math.h>
double freshness(double days,double decay){ return exp(-decay*days); }
double quality(double v,double f,double c,double l,double m){ return 100*(0.25*v+0.18*f+0.20*c+0.22*l+0.15*m); }
int main(void){ printf("test_name,value\nfreshness_3_days,%.4f\npipeline_quality_score,%.3f\n", freshness(3,0.025), quality(.92,.86,.90,.88,.82)); return 0; }
