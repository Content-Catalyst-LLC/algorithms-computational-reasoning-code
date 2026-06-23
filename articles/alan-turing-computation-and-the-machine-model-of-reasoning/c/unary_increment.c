#include <stdio.h>
#include <string.h>

int main(void) {
    char tape[32] = "111_";
    int i = 0;
    while (tape[i] == '1') {
        i++;
    }
    tape[i] = '1';
    tape[i + 1] = '_';
    tape[i + 2] = '\0';
    printf("incremented_tape=%s\n", tape);
    return 0;
}
