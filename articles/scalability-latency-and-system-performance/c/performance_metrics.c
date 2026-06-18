#include <stdio.h>
double response_time(double n,double q,double c,double s,double o){ return n+q+c+s+o; }
double throughput(double completed,double seconds){ return seconds == 0 ? 0 : completed/seconds; }
double utilization(double arrival,double service){ return service == 0 ? 0 : arrival/service; }
double little_law(double arrival,double time){ return arrival*time; }
int main(void){ printf("test_name,value\nresponse_time_ms,%.3f\nthroughput,%.3f\nutilization,%.3f\nlittle_law_items,%.3f\n", response_time(45,20,85,35,15), throughput(12000,60), utilization(180,200), little_law(180,.45)); return 0; }
