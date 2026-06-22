#include <iostream>

int main() {
    double present_fields = 11.0;
    double required_fields = 12.0;
    double score = present_fields / required_fields;
    std::cout << "metadata_completeness_score=" << score << "\n";
    return 0;
}
