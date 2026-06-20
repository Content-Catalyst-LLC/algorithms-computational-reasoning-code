#include <iostream>
double density(double nodes, double edges){ return nodes <= 1 ? 0 : edges/(nodes*(nodes-1)); }
int main(){ std::cout << "test_name,value\nnode_count,5\nedge_count,7\ndensity," << density(5,7) << "\nmanual_shortest_path_cost,5.5\n"; }
