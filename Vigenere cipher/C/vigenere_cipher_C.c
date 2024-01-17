#include <stdio.h>
#include <ctype.h>
#include <string.h>

int isUppercase(char c);

int main() {
    printf("C program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n\n");

    // Declaring data to be used for encryption and decryption.
    char alphabets[] = "abcdefghijklmnopqrstuvwxyz";
    int alphaIndex[26] = {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25
    };

// Handling input for the Cipher key. Note minus sign before key for decryption and plus sign for encryption.
    char key[20];
    int decrypt = 0;
    while (1) {
        printf("Key (Enter a minus sign before key for decryption and plus sign for encryption e.g +key, -key): ");
        scanf("%s", key);
        int valid = strlen(key) > 1 && (key[0] == '+' || key[0] == '-');
        for (int i = 1; i < strlen(key); i++) {
            if (!(key[i] >= 'a' && key[i] <= 'z') && !(key[i] >= 'A' && key[i] <= 'Z')) {
                valid = 0;
                break;
            }
        }
        if (valid) {
            decrypt = (key[0] == '-') ? 1 : 0;
            break;
        }
        printf("Invalid Key\n");
    }

    // Collecting string to be decrypted or encrypted.
    if (decrypt) {
        printf("Encrypted Text: ");
    } else {
        printf("Plain Text: ");
    }
    char plainText[100];
    scanf(" %[^\n]s", plainText);

    // Working the magic.
    int keyLength = strlen(key) - 1;
    int counter = 1;
    for (int i = 0; i < strlen(plainText); i++) {
        char c = plainText[i];
        char c2 = key[counter];
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            int newIdx = (alphaIndex[(isUppercase(c) ? c - 'A' : c - 'a')] + alphaIndex[(isUppercase(c2) ? c2 - 'A' : c2 - 'a')]) % 26;
            int decryptIdx = (alphaIndex[(isUppercase(c) ? c - 'A' : c - 'a')] - alphaIndex[(isUppercase(c2) ? c2 - 'A' : c2 - 'a')] + 26) % 26;
            int newIndex = decrypt ? decryptIdx : newIdx;
            counter = 1 + ((counter + 1) % keyLength);
            printf("%c", isUppercase ? ('A' + newIndex) : ('a' + newIndex));
        } else {
            printf("%c", c);
        }
    }

    printf("\n[Program finished]\n");

    return 0;
}

int isUppercase(char c){
    return (c >= 'A' && c <= 'Z') ? 1 : 0;
}