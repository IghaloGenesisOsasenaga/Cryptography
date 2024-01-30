# JS Vanilla
## Caesarean Cipher - JavaScript Program

This JavaScript program provides an Encrypter and Decrypter for the Caesarean Cipher.

### Usage

1. Run the program in a JavaScript environment.
2. Input the shift value when prompted. Enter a negative integer for decryption.
3. Provide the plain or encrypted text as instructed.
4. View the result in the console and as an alert.

## Code Highlights

### Shift Input
```javascript
// Handling input for the Cipher shift.
let shift = null;
while (true) {0
    // Prompt for shift input and validate for a valid integer.
}

// Collecting string to be decrypted or encrypted.
let plainText;
// Prompt for text input based on the shift value.
```

### Encryption/Decryption Logic
```javascript
// Loop through each character in the input text.
// Check if it's an alphabet, then apply the shift.
// Handle uppercase and lowercase characters accordingly.
```

### Output
```javascript
// Displayed result in the console and as an alert.
```

## Example
```javascript
main();
```

---

# JS with HTML
## Caesarean Cipher - JavaScript Program with HTML

This JavaScript program with HTML provides a user-friendly interface for the Caesarean Cipher.

### Usage

1. Open the HTML file in a web browser.
2. Input the shift value (positive for encryption, negative for decryption).
3. Choose the decryption option if needed.
4. Enter the text to be processed.
5. Click the "Run" button to see the result.

### HTML Structure

- Input field for shift value, decryption checkbox, and text area.
- Run button to initiate the encryption/decryption process.

## JavaScript Functions

### `validate(shift_inp, shift_label, button)`
- Validates the shift input for a positive integer.
- Updates the shift label and enables/disables the run button accordingly.

### `encrypt_or_decrypt(shift, text, decrypt)`
- Handles encryption or decryption based on user input.
- Updates the text area with the result.

### `main()`
- Initializes event listeners and sets up the main functionality.

## Example
```javascript
document.addEventListener("DOMContentLoaded", main);
```

# HTML
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Caesarean Cipher</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="caesar_cipher.css">
    </head>
    <body>
        <!-- HTML content as provided in your code -->
    </body>
</html>
```

Ensure to follow the instructions displayed on the webpage for a smooth experience.
Feel free to contribute or report issues on [Github](https://github.com/Genesis-js/Cryptography)