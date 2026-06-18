#include <iostream>
double schema_quality(double f,double k,double c,double m,double l){ return 100*(0.22*f+0.20*k+0.20*c+0.20*m+0.18*l); }
int main(){ std::cout << "test_name,value\nschema_quality_score," << schema_quality(.90,.85,.80,.88,.82) << "\n"; }
