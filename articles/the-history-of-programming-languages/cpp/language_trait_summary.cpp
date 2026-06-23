#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, std::string> languages = {
        {"Fortran", "scientific numerical programming"},
        {"Lisp", "symbolic computation"},
        {"SQL", "declarative data querying"},
        {"Rust", "memory-safe systems programming"}
    };
    for (const auto& item : languages) {
        std::cout << item.first << ": " << item.second << "\n";
    }
}
