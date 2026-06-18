#include <stdio.h>
double speedup(double s, double p){ return 1.0 / (s + ((1.0-s)/p)); }
int main(void){ double sp=speedup(0.10,16.0); printf("test_name,value\nspeedup_p16_s010,%.6f\nefficiency_p16_s010,%.6f\n", sp, sp/16.0); return 0; }
