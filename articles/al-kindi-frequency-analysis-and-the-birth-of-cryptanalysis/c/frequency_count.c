#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE";
    int counts[26] = {0};
    for (size_t i = 0; i < strlen(text); i++) {
        char ch = (char)tolower((unsigned char)text[i]);
        if (ch >= 'a' && ch <= 'z') {
            counts[ch - 'a']++;
        }
    }
    for (int i = 0; i < 26; i++) {
        if (counts[i] > 0) {
            printf("%c,%d\n", 'a' + i, counts[i]);
        }
    }
    return 0;
}
