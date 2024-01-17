#include <iostream>
#include <cctype>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    cout << "C++ program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n";

    // Declaring data to be used for encryption and decryption.
    string alphabets = "abcdefghijklmnopqrstuvwxyz";
    unordered_map<char, int> alphaIndex;
    for (int i = 0; i < alphabets.length(); i++) {
        alphaIndex[alphabets[i]] = i;
    }

    // Handling input for the Cipher key. Note minus sign before key for decryption and plus sign for encryption.
    string key;
    bool decrypt = false;
    while (true) {
        cout << "Key (Enter a minus sign before key for decryption and plus sign for encryption e.g +key, -key): ";
        cin >> key;
        bool valid = key.length() > 1 && (key[0] == '+' || key[0] == '-');
        for (int i = 1; i < key.length(); i++) {
            if (!(isalpha(key[i]))) {
                valid = false;
                break;
            }
        }
        if (valid) {
            decrypt = key[0] == '-';
            break;
        }
        cout << "Invalid Key\n";
    }

    // Collecting string to be decrypted or encrypted.
    if (decrypt) {
        cout << "Encrypted Text: ";
    } else {
        cout << "Plain Text: ";
    }
    cin.ignore(); // clear buffer
    string plainText;
    getline(cin, plainText);

    // Working the magic.
    int keyLength = key.length() - 1;
    int counter = 1;
    string result = "";
    for (char c : plainText) {
        if (isalpha(c)) {
            bool isUppercase = isupper(c);
            int newIdx = (alphaIndex[tolower(c)] + alphaIndex[tolower(key[counter])]) % 26;
            int decryptIdx = (alphaIndex[tolower(c)] - alphaIndex[tolower(key[counter])] + 26) % 26;
            int newIndex = decrypt ? decryptIdx : newIdx;
            counter = 1 + ((counter + 1) % keyLength);
            result += isUppercase ? toupper(alphabets[newIndex]) : alphabets[newIndex];
        } else {
            result += c;
        }
    }

    cout << result + "\n[Program finished]\n";

    return 0;
}