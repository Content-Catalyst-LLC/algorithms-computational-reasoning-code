#include <stdio.h>

int main(void) {
    const char *languages[][2] = {
        {"Fortran", "scientific numerical programming"},
        {"Lisp", "symbolic computation"},
        {"SQL", "declarative data querying"},
        {"Rust", "memory-safe systems programming"}
    };
    for (int i = 0; i < 4; ++i) {
        printf("%s: %s\n", languages[i][0], languages[i][1]);
    }
    return 0;
}
