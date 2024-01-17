function main() {
    console.log("JavaScript program for working with the Vigenere Cipher. (Encrypter and Decrypter)\n");
    alert("JavaScript program for working with the Vigenere Cipher. (Encrypter and Decrypter)\n");

    // Declaring data to be used for encryption and decryption.
    const alphabets = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z'
    ];
    const alphaIndex = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
        'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
        'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
        'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
        'z': 25
    };

    // Handling input for the Cipher key. Note minus sign before key for decryption and plus sign for encryption.
    let key = null;
    let decrypt = false;
    while (true) {
        key = prompt('Key (Enter a minus sign before key for decryption and plus sign for encryption): ');
        let keyLen = key.length
        let valid = keyLen > 1 && (key[0] == '+' || key[0] == '-');
        for (let i=1; i<keyLen; ++i) {
            let char = key[i];
            if (!char.match(/[a-zA-Z]$/)) {
                valid = false;
                break;
            }
        }
        if (valid){
            decrypt = key[0] == '-';
            break;
        }
        alert('Invalid Key');
    }

    // Collecting string to be decrypted or encrypted.
    let plainText;
    if (decrypt) plainText = prompt("Encrypted Text: ");
    else plainText = prompt("Plain Text: ");

    // Working the magic.
    let result = '';
    let key_length = key.length-1;
    let counter = 1;
    for (let char of plainText) {
        if (char.match(/[a-zA-Z]$/)){
            let isUppercase = (char == char.toUpperCase());
            let newIndex = (alphaIndex[char.toLowerCase()] + alphaIndex[key[counter].toLowerCase()]) % 26;
            if(decrypt){
                newIndex = (alphaIndex[char.toLowerCase()] - alphaIndex[key[counter].toLowerCase()] + 26) % 26;
            }
            counter = 1 + ((++counter) % key_length);
            result += isUppercase ? alphabets[newIndex].toUpperCase() : alphabets[newIndex];
        } else {
            result += char;
        }
    }

    console.log(result + "\n[Program finished]");
    alert(result);
}

main();