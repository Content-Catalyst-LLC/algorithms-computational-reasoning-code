#include <iostream>
#include <algorithm>
double selection_rows(double rows,double selectivity){ return rows*selectivity; }
double join_rows(double l,double r,double ld,double rd){ return (l*r)/std::max(ld,rd); }
int main(){ std::cout << "test_name,value\nselection_estimated_rows," << selection_rows(1000000,0.012) << "\njoin_estimated_rows," << join_rows(500000,200000,50000,40000) << "\n"; }
