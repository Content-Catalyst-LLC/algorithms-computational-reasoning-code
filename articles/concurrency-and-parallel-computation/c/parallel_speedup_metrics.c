#include <stdio.h>
double speedup(double t1,double tp){ return tp == 0 ? 0 : t1/tp; }
double amdahl(double p,double s){ return p == 0 ? 0 : 1.0/(s+((1.0-s)/p)); }
double efficiency(double p,double sp){ return p == 0 ? 0 : sp/p; }
int main(void){ double sp=speedup(120,28); printf("test_name,value\nobserved_speedup_120_to_28,%.4f\namdahl_speedup_8_workers,%.4f\nefficiency_8_workers,%.4f\n", sp, amdahl(8,0.12), efficiency(8,sp)); return 0; }
