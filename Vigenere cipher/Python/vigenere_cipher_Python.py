from re import match

def main():
    print("Python program for working with the Vigenere Cipher. (Encrypter and Decrypter)\n")
    
    # Declaring data to be used for encryption and decryption.
    alphabets = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z'
    ]
    alpha_index = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
        'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
        'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
        'p':15, 'q':16, 'r':17, 's':18, 't':19,
        'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
        'z':25
    }
    
    # Handling input for the Cipher key. Note minus sign before key for decryption and plus sign for encryption.
    key = None
    decrypt = False
    while True:
        key = input('Key (Enter a minus sign before key for decryption and plus sign for encryption e.g +key, -key): ')
        key_len = len(key)
        valid = key_len > 1 and (key[0] == '+' or key[0] == '-')
        for i in range(1, key_len):
            char = key[i]
            if not (match(r'[a-zA-Z]', char)):
                valid = False
                break
        if valid:
            decrypt = key[0] == '-'
            break
        print("Invalid Key")
    
    # Collecting string to be decrypted or encrypted.
    if decrypt:
        print("Encrypted Text: ", end='')
    else:
        print("Plain Text: ", end='')
    plain_text = input()
    
    # Working the magic.
    key_length = len(key)-1
    counter = 1
    for char in plain_text:
        if char.isalpha():
            is_uppercase = char.isupper()
            new_index = (alpha_index[char.lower()] + alpha_index[key[counter].lower()]) % 26
            if decrypt:
                new_index = (alpha_index[char.lower()] - alpha_index[key[counter].lower()]) % 26
            counter = 1 + ((counter+1) % key_length)
            if is_uppercase:
                print(alphabets[new_index].upper(), end='')
            else:
                print(alphabets[new_index], end='')
        else:
            print(char, end='')
    
    print("\n[Program finished]")

main()