#include <stdio.h>
double density(double nodes, double edges){ return nodes <= 1 ? 0 : edges/(nodes*(nodes-1)); }
int main(void){ printf("test_name,value\nnode_count,5\nedge_count,7\ndensity,%.6f\nmanual_shortest_path_cost,5.5\n", density(5,7)); return 0; }
