#include <stdio.h>
double precision(double tp,double retrieved){ return retrieved == 0 ? 0 : tp/retrieved; }
double recall(double tp,double relevant){ return relevant == 0 ? 0 : tp/relevant; }
int main(void){ printf("test_name,value\nprecision,%.4f\nrecall,%.4f\n", precision(2,3), recall(2,2)); return 0; }
