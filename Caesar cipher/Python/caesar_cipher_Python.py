def main():
    print("Python program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n")
    
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
    
    # Handling input for the Cipher shift. Note negative shift for decryption and positive for encryption.
    shift = None
    while True:
        test = input('Shift Enter a negative integer for decryption): ').replace(" ", "")
        valid = True
        for char in test:
            if not (char.isdigit()) and char != '-':
                valid = False
                break
        
        if '-' in test:
            num_of_neg_sign = test.count('-')
            if num_of_neg_sign > 1 or test[0] != '-':
                valid = False
        
        if valid and test != '':
            shift = int(test) % 26
            break
        else:
            print("Enter a valid integer")
    
    # Collecting string to be decrypted or encrypted.
    if shift < 0:
        print("Encrypted Text: ", end='')
    else:
        print("Plain Text: ", end='')
    plain_text = input()
    
    # Working the magic.
    for char in plain_text:
        if char.isalpha():
            is_uppercase = char.isupper()
            new_index = (alpha_index[char.lower()] + shift) % 26
            if is_uppercase:
                print(alphabets[new_index].upper(), end='')
            else:
                print(alphabets[new_index], end='')
        else:
            print(char, end='')
    
    print("\n[Program finished]")

main()