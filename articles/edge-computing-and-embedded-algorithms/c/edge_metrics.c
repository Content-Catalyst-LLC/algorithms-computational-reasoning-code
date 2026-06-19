#include <stdio.h>
double edge_response_time(double s,double f,double c,double a){ return s+f+c+a; }
double cloud_response_time(double s,double u,double c,double d,double a){ return s+u+c+d+a; }
double battery_life(double b,double p){ return p == 0 ? 0 : b/p; }
const char* local_action(double signal,double threshold){ return signal >= threshold ? "alert" : "monitor"; }
int main(void){ printf("test_name,value\nedge_response_time_ms,%.3f\ncloud_response_time_ms,%.3f\nbattery_life_hours,%.3f\nlocal_action,%s\n", edge_response_time(8,6,14,5), cloud_response_time(8,90,60,90,5), battery_life(12,.08), local_action(.82,.75)); return 0; }
