#include <stdio.h>
int mq(int n){return n/2+1;} int ft(int n){return (n-1)/2;} int bft(int f){return 3*f+1;} int main(void){printf("test_name,value\nmajority_quorum_5_nodes,%d\ncrash_fault_tolerance_5_nodes,%d\nbyzantine_replicas_for_2_faults,%d\n",mq(5),ft(5),bft(2));return 0;}
