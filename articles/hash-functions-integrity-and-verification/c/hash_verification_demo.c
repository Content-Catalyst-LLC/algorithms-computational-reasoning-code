#include <stdio.h>
#include <string.h>

unsigned long teaching_checksum(const char *s) {
    unsigned long total = 0;
    for (size_t i = 0; i < strlen(s); i++) {
        total = (total + (unsigned long)(unsigned char)s[i] * (i + 1)) % 1000003UL;
    }
    return total;
}

int main(void) {
    const char *original = "verified artifact manifest";
    const char *altered = "verified artifact manifest!";
    printf("original checksum=%lu\n", teaching_checksum(original));
    printf("altered checksum=%lu\n", teaching_checksum(altered));
    printf("match=%s\n", teaching_checksum(original) == teaching_checksum(altered) ? "true" : "false");
    return 0;
}
