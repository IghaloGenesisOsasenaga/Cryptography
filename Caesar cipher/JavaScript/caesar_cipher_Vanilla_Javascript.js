function main() {
    console.log("JavaScript program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n");
    alert("JavaScript program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n");

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

    // Handling input for the Cipher shift. Note negative shift for decryption and positive for encryption.
    let shift = null;
    while (true) {
        let test = prompt('Shift (Enter a negative integer for decryption): ').replace(" ", "");
        let valid = true;
        for (let char of test) {
            if (!char.match(/\d/) && char !== '-') {
                valid = false;
                break;
            }
        }

        if (test.includes('-')) {
            let num_of_neg_sign = (test.match(/-/g) || []).length;
            if (num_of_neg_sign > 1 || test[0] !== '-') {
                valid = false;
            }
        }

        if (valid && test !== '') {
            shift = parseInt(test) % 26;
            break;
        } else {
            alert("Enter a valid integer");
        }
    }

    // Collecting string to be decrypted or encrypted.
    let plainText;
    if (shift < 0) {
        console.log("Encrypted Text: ");
        plainText = prompt("Encrypted Text: ");
    } else {
        console.log("Plain Text: ");
        plainText = prompt("Plain Text: ");
    }

    // Working the magic.
    let result = '';
    for (let char of plainText) {
        if (char.match(/[a-zA-Z]/)) {
            let isUppercase = char === char.toUpperCase();
            let newIndex = (alphaIndex[char.toLowerCase()] + shift + 26) % 26;
            result += isUppercase ? alphabets[newIndex].toUpperCase() : alphabets[newIndex];
        } else {
            result += char;
        }
    }

    console.log(result + "\n[Program finished]");
    alert(result);
}

main();