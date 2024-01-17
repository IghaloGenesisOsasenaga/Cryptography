function main(){
    // Collecting user inputs.
    const key = document.querySelector("#key");
    const text = document.querySelector("#text");
    const button = document.querySelector("#run_btn");
    const keyLabel = document.querySelector("#key_label");
    const decrypt = document.querySelector("#decrypt");
    
    // Handling input for the Cipher key. Note negative key for decryption and positive for encryption.
    //let key = None;
    key.addEventListener("input", () => {validate(key, keyLabel, button)});
    
    // Working the magic.
    button.addEventListener("click", () => {
        if (key.checkValidity()) encrypt_or_decryt(key.value, text, decrypt);
        else alert("Invalid Key")
    });
}

function validate(key_inp, key_label, button){
    let valid = key_inp.checkValidity();
    
    if (valid){
        key_label.innerText = "Cipher Key.";
    } else {
        key_label.innerText = "Enter a valid text with alphabets only";
    }
}

function encrypt_or_decryt(key, text, decrypt){
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
        'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
        'p':15, 'q':16, 'r':17, 's':18, 't':19,
        'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
        'z':25
    };
    
    let result = "";
    let key_length = key.length;
    let counter = 0;
    
    for (const char of text.value){
        if (char.match(/[a-zA-Z]$/)){
            let isUppercase = (char == char.toUpperCase());
            let newIndex = (alphaIndex[char.toLowerCase()] + alphaIndex[key[counter].toLowerCase()]) % 26;
            if(decrypt.checked == true){
                newIndex = (alphaIndex[char.toLowerCase()] - alphaIndex[key[counter].toLowerCase()] + 26) % 26;
            }
            counter = (++counter) % key_length;
            result += isUppercase ? alphabets[newIndex].toUpperCase() : alphabets[newIndex];
        } else {
            result += char;
        }
    }
    text.value = result;
}

document.addEventListener("DOMContentLoaded", main);