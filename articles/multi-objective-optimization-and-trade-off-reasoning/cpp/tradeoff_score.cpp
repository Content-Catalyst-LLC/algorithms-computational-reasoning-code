#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::pair<std::string,double>> scores{{"A",0.52},{"B",0.49},{"C",0.82},{"D",0.35}};
    for (const auto& s : scores) std::cout << s.first << " " << s.second << "\n";
    return 0;
}
