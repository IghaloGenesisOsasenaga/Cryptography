#include <iostream>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    cout << "C++ program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n\n";
    // Declaring data to be used for encryption and decryption.
    string alphabets = "abcdefghijklmnopqrstuvwxyz";
    unordered_map<char, int> alphaIndex = {
        {'a', 0}, {'b', 1}, {'c', 2}, {'d', 3}, {'e', 4},
        {'f', 5}, {'g', 6}, {'h', 7}, {'i', 8}, {'j', 9},
        {'k', 10}, {'l', 11}, {'m', 12}, {'n', 13}, {'o', 14},
        {'p', 15}, {'q', 16}, {'r', 17}, {'s', 18}, {'t', 19},
        {'u', 20}, {'v', 21}, {'w', 22}, {'x', 23}, {'y', 24},
        {'z', 25}
    };

    // Handling input for the Cipher shift. Note negative shift for decryption and positive for encryption.
    int shift = 0;
    while (true) {
        cout << "Shift (Enter a negative integer for decryption): ";
        string inputShift;
        getline(cin, inputShift);
        inputShift.erase(remove_if(inputShift.begin(), inputShift.end(), ::isspace), inputShift.end());
        
        bool valid = true;
        for (char c : inputShift) {
            if (!isdigit(c) && c != '-') {
                valid = false;
                break;
            }
        }
        
        int num_of_neg_sign = count(inputShift.begin(), inputShift.end(), '-');
        if (inputShift.find('-') != string::npos){
            if (num_of_neg_sign > 1 || inputShift[0] != '-') {
                valid = false;
            }
        }
        
        if (valid && inputShift != "") {
            shift = stoi(inputShift) % 26;
            break;
        }
        cout << "Enter a valid integer\n";
    }

    // Collecting string to be decrypted or encrypted.
    string text;
    if (shift < 0){
        shift += 26;
        cout << "Encrypted Text: ";
    } else{
        cout << "Plain Text: ";
    }
    getline(cin, text);

    // Working the magic.
    for (char c : text) {
        if (isalpha(c)) {
            bool is_uppercase = isupper(c);
            int newIndex = (alphaIndex[tolower(c)] + shift) % 26;
            if (is_uppercase) {
                cout << toupper(alphabets[newIndex]);
            } else {
                cout << alphabets[newIndex];
            }
        } else {
            cout << c;
        }
    }

    cout << "\n[Program finished]\n";

    return 0;
}