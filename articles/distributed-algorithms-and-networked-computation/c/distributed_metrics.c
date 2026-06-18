#include <stdio.h>
#include <math.h>
int quorum_size(int n){ return n/2 + 1; }
int crash_fault_tolerance(int n){ return (n-1)/2; }
double availability(double replicas,double node_availability){ return 1.0 - pow(1.0-node_availability, replicas); }
double latency(double compute,double network,double queue){ return compute+network+queue; }
int main(void){ printf("test_name,value\nquorum_5_nodes,%d\nfault_tolerance_5_nodes,%d\navailability_3_replicas,%.6f\ndistributed_latency_ms,%.3f\n", quorum_size(5), crash_fault_tolerance(5), availability(3,0.99), latency(35,80,20)); return 0; }
