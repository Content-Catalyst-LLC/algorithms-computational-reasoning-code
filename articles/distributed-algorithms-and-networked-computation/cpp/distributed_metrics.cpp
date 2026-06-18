#include <iostream>
#include <cmath>
int quorum_size(int n){ return n/2 + 1; }
int crash_fault_tolerance(int n){ return (n-1)/2; }
double availability(double replicas,double node_availability){ return 1.0 - std::pow(1.0-node_availability, replicas); }
double latency(double compute,double network,double queue){ return compute+network+queue; }
int main(){ std::cout << "test_name,value\nquorum_5_nodes," << quorum_size(5) << "\nfault_tolerance_5_nodes," << crash_fault_tolerance(5) << "\navailability_3_replicas," << availability(3,0.99) << "\ndistributed_latency_ms," << latency(35,80,20) << "\n"; }
