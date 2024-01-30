#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    printf("C program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n\n");

    // Declaring data to be used for encryption and decryption.
    char alphabets[] = "abcdefghijklmnopqrstuvwxyz";
    int alphaIndex[26] = {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25
    };

    // Handling input for the Cipher shift. Note negative shift for decryption and positive for encryption.
    int shift = 0;
    while (1) {
        printf("Shift (Enter a negative integer for decryption): ");
        char inputShift[256];
        fgets(inputShift, sizeof(inputShift), stdin);
        inputShift[strcspn(inputShift, "\n")] = '\0';  // Remove newline character

        int valid = 1;
        for (int i = 0; inputShift[i] != '\0'; i++) {
            if (!isdigit(inputShift[i]) && inputShift[i] != '-') {
                valid = 0;
                break;
            }
        }

        int num_of_neg_sign = 0;
        for (int i = 0; inputShift[i] != '\0'; i++) {
            if (inputShift[i] == '-') {
                num_of_neg_sign++;
            }
        }
        
        if (strchr(inputShift, '-') != NULL) {
            if (num_of_neg_sign > 1 || inputShift[0] != '-') {
                valid = 0;
            }
        }

        if (valid && strcmp(inputShift, "") != 0) {
            shift = atoi(inputShift) % 26;
            break;
        }
        printf("Enter a valid integer\n");
    }

    // Collecting string to be decrypted or encrypted.
    char text[256];
    if (shift < 0) {
        shift += 26;
        printf("Encrypted Text: ");
    } else {
        printf("Plain Text: ");
    }
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';  // Remove newline character

    // Working the magic.
    for (int i = 0; text[i] != '\0'; i++) {
        char c = text[i];
        if (isalpha(c)) {
            int is_uppercase = isupper(c);
            int newIndex = (alphaIndex[tolower(c) - 'a'] + shift) % 26;
            if (is_uppercase) {
                printf("%c", toupper(alphabets[newIndex]));
            } else {
                printf("%c", alphabets[newIndex]);
            }
        } else {
            printf("%c", c);
        }
    }

    printf("\n[Program finished]\n");

    return 0;
}