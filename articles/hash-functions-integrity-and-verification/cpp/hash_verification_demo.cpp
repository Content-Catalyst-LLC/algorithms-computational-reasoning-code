#include <iostream>
#include <string>

unsigned long teaching_checksum(const std::string& s) {
    unsigned long total = 0;
    for (std::size_t i = 0; i < s.size(); ++i) {
        total = (total + static_cast<unsigned long>(static_cast<unsigned char>(s[i])) * (i + 1)) % 1000003UL;
    }
    return total;
}

int main() {
    std::string original = "verified artifact manifest";
    std::string altered = "verified artifact manifest!";
    std::cout << "original checksum=" << teaching_checksum(original) << "\n";
    std::cout << "altered checksum=" << teaching_checksum(altered) << "\n";
    std::cout << "match=" << (teaching_checksum(original) == teaching_checksum(altered) ? "true" : "false") << "\n";
    return 0;
}
