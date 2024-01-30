# Vigenere Cipher in C++ Documentation

## Overview

This C++ program implements the Vigenere Cipher, serving as both an encrypter and decrypter. It takes user input for the key (a minus sign before key for decryption and plus sign for encryption) and the text to be encrypted or decrypted.

## Usage

1. Compile the program:

    ```bash
    g++ vigenere_cipher.cpp -o vigenere_cipher

    ```

2. Run the program:

    ```bash
    ./vigenere_cipher

    ```

3. Input the key (e.g., +foo or -foo) when prompted.

4. Enter the text to be encrypted or decrypted.

## Example

1. Encrypting text:
    ```
    Key: +foo
    Plain Text: Hello
    ```
2. Decrypting text:
    ```
    Key: -foo
    Encrypted Text: Mszqc
    ```

### Notes
* The program handles both uppercase and lowercase letters.
* Non-alphabetic characters remain unchanged.
* The key must consist of only alphabetic characters.

Feel free to contribute or report issues on [GitHub](https://github.com/Genesis-js/Cryptography/issues)