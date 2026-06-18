#include <iostream>
double total_latency(double c,double s,double n,double q,double o){ return c+s+n+q+o; }
double nominal_capacity(double nodes,double cap){ return nodes*cap; }
double unit_cost(double c,double s,double n,double m,double o,double completed){ return completed == 0 ? 0 : (c+s+n+m+o)/completed; }
int main(){ std::cout << "test_name,value\ncloud_response_latency_ms," << total_latency(80,45,60,25,15) << "\nnominal_capacity," << nominal_capacity(12,250) << "\nunit_cost," << unit_cost(120,35,25,90,18,144000) << "\n"; }
