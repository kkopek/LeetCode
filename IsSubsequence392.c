#include <string.h>

// Fucntion flow:
// 1. Check if substring is empty. If so, its automatically a subsequence
// 2. Set the pointer curr to zero. curr points to the current character in substring
// 3. Loop over the t string, if the match found increment the curr. 
// 4. If curr == the size of s substring, that means all characters were matched return true
// 5. If loop terminated and curr != size of s, return false
bool isSubsequence(char* s, char* t) {
    size_t lenT = strlen(t);
    size_t lenS = strlen(s);

    if (lenS == 0) {
        return true;
    }

    int curr = 0;
    for (int i = 0; i < lenT; i++) {
        if (s[curr] == t[i]) {
            curr ++;
            if (curr == lenS) {
                return true;
            }
        }
    }

    return false;
}