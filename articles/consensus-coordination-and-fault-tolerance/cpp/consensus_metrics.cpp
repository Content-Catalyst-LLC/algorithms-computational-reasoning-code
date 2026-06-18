#include <iostream>
int mq(int n){return n/2+1;} int ft(int n){return (n-1)/2;} int bft(int f){return 3*f+1;} int main(){std::cout<<"test_name,value\nmajority_quorum_5_nodes,"<<mq(5)<<"\ncrash_fault_tolerance_5_nodes,"<<ft(5)<<"\nbyzantine_replicas_for_2_faults,"<<bft(2)<<"\n";}
