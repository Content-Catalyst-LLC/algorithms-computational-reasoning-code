#include <stdio.h>

int main(void) {
    const char *source = "ADD PAYROLL-TOTAL TO TAX-BASE";
    printf("source=%s\n", source);
    printf("tokens=[ADD, PAYROLL-TOTAL, TO, TAX-BASE]\n");
    printf("target_code=machine-specific instruction sequence\n");
    return 0;
}
