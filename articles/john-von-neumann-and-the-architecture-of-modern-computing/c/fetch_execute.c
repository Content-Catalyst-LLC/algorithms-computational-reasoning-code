#include <stdio.h>
#include <string.h>

typedef struct {
    const char *op;
    int arg;
} Instruction;

int main(void) {
    Instruction program[] = {{"LOAD", 2}, {"ADD", 3}, {"STORE", 0}, {"HALT", 0}};
    int acc = 0;
    int n = sizeof(program) / sizeof(program[0]);
    for (int i = 0; i < n; i++) {
        if (strcmp(program[i].op, "LOAD") == 0) acc = program[i].arg;
        else if (strcmp(program[i].op, "ADD") == 0) acc += program[i].arg;
        else if (strcmp(program[i].op, "STORE") == 0) printf("store address=%d value=%d\n", program[i].arg, acc);
        else if (strcmp(program[i].op, "HALT") == 0) {
            printf("halt accumulator=%d\n", acc);
            break;
        }
    }
    return 0;
}
