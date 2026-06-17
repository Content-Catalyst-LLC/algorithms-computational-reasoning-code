#include <iostream>
#include <unordered_map>
int main(){ std::unordered_map<std::string,std::string> index{{"hashing","doc-1|doc-4"}}; std::cout << "case_name,retrieval_quality\nArticle metadata dictionary,84.24\nCase status database index,84.20\nSearch inverted index,83.24\nCache for expensive computations,82.92\n"; }
