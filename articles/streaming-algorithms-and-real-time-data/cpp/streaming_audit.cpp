#include <iostream>
int main(){ double arrival=90.0, processing=100.0; std::cout << "test_name,value\nutilization," << arrival/processing << "\nstable," << (arrival < processing ? "true" : "false") << "\n"; }
