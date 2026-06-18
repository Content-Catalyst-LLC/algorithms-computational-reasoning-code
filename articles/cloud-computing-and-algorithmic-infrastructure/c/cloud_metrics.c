#include <stdio.h>
double total_latency(double c,double s,double n,double q,double o){ return c+s+n+q+o; }
double nominal_capacity(double nodes,double cap){ return nodes*cap; }
double unit_cost(double c,double s,double n,double m,double o,double completed){ return completed == 0 ? 0 : (c+s+n+m+o)/completed; }
int main(void){ printf("test_name,value\ncloud_response_latency_ms,%.3f\nnominal_capacity,%.3f\nunit_cost,%.6f\n", total_latency(80,45,60,25,15), nominal_capacity(12,250), unit_cost(120,35,25,90,18,144000)); return 0; }
