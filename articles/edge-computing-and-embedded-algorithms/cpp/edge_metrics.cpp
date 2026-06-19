#include <iostream>
#include <string>
double edge_response_time(double s,double f,double c,double a){ return s+f+c+a; }
double cloud_response_time(double s,double u,double c,double d,double a){ return s+u+c+d+a; }
double battery_life(double b,double p){ return p == 0 ? 0 : b/p; }
std::string local_action(double signal,double threshold){ return signal >= threshold ? "alert" : "monitor"; }
int main(){ std::cout << "test_name,value\nedge_response_time_ms," << edge_response_time(8,6,14,5) << "\ncloud_response_time_ms," << cloud_response_time(8,90,60,90,5) << "\nbattery_life_hours," << battery_life(12,.08) << "\nlocal_action," << local_action(.82,.75) << "\n"; }
