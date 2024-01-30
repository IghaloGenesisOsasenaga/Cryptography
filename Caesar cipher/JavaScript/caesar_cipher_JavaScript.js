function main(){
    // Collecting user inputs.
    const shift = document.querySelector("#shift");
    const text = document.querySelector("#text");
    const button = document.querySelector("#run_btn");
    const shiftLabel = document.querySelector("#shift_label")
    const decrypt = document.querySelector("#decrypt");
    
    // Handling input for the Cipher shift. Note negative shift for decryption and positive for encryption.
    //let shift = None;
    shift.addEventListener("input", () => {validate(shift, shiftLabel, button)})
    
    // Working the magic.
    button.addEventListener("click", () => {encrypt_or_decryt(shift.value, text, decrypt)})
}

function validate(shift_inp, shift_label, button){
    let valid = shift_inp.checkValidity();
    if (shift_inp.value < 0){
        valid = false;
    }
    
    if (valid){
        shift_label.innerText = "Cipher Shift.";
        button.disabled = false;
    } else {
        shift_label.innerText = "Enter a valid integer";
        button.disabled = true;
    }
}

function encrypt_or_decryt(shift, text, decrypt){
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
    
    for (const char of text.value){
        if (char.match(/^[a-zA-Z]$/)){
            let isUppercase = (char == char.toUpperCase());
            let newIndex = (alphaIndex[char.toLowerCase()] + parseInt(shift)) % 26;
            if(decrypt.checked == true){
                newIndex = (alphaIndex[char.toLowerCase()] - parseInt(shift)) % 26;
                if (newIndex < 0){
                    newIndex += 26;
                }
            }
            if (isUppercase){
                result += alphabets[newIndex].toUpperCase();
            } else {
                result += alphabets[newIndex];
            }
        } else {
            result += char;
        }
    }
    text.value = result;
}

document.addEventListener("DOMContentLoaded", main);