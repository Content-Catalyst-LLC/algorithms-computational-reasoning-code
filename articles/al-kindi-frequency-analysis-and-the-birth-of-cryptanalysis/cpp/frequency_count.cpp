#include <algorithm>
#include <cctype>
#include <iostream>
#include <map>
#include <string>

int main() {
    std::string text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE";
    std::map<char, int> counts;
    for (char ch : text) {
        unsigned char uch = static_cast<unsigned char>(ch);
        if (std::isalpha(uch)) {
            counts[static_cast<char>(std::tolower(uch))]++;
        }
    }
    for (const auto& [symbol, count] : counts) {
        std::cout << symbol << "," << count << "\n";
    }
    return 0;
}
