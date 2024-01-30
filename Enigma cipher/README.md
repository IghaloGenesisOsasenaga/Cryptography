# Enigma Emulator Documentation

## Introduction
The Enigma Emulator is a Python implementation of the Enigma machine, a historical encryption device used during World War II. This emulator allows users to encrypt and decrypt messages using the Enigma machine's principles. The emulator supports customizable rotor order, plugboard sequence, ring settings, starting positions, and text input.

## Usage

### Input Format
- **Rotor Order:** Specify the rotor order using Roman numerals (e.g., I V III).
- **Plugboard Sequence:** Define the plugboard sequence by swapping pairs of letters (e.g., EU RT FI GH JK LM NQ PD OA WV BZ SY XC).
- **Ring Settings:** Set the ring settings as either Roman numerals or numbers separated by spaces (e.g., 2 17 9 or BQI).
- **Starting Positions:** Provide the starting positions as Roman numerals or letters separated by spaces (e.g., 6 4 2 or FDB).
- **Text:** Enter the text to be encrypted or decrypted. Prefix the text with "+" for encryption or "-" for decryption. For encrypted text, the pattern must match the specified format.

### Output
The emulator prints the result in all capital letters. In decryption, special characters may replace null sequences (e.g., space represented by 'HRL').

### Example
```python
# Example Input for encryption
Rotor order: I V III
Plugboard sequence: EU RT FI GH JK LM NQ PD OA WV BZ SY XC
Ring settings: 2 17 9
Starting positions: 6 4 2
Text: +Some normal text

# Example Output
ENCR YPTE DHRL OUTP UTHR LINH RLAL LHRL CAPS

# Example Input for decryption
Rotor order: I V III
Plugboard sequence: EU RT FI GH JK LM NQ PD OA WV BZ SY XC
Ring settings: 2 17 9
Starting positions: 6 4 2
Text: -Some encrypted text

# Example Output
DECRYPTED TEXT IN ALL CAPS
```

## Customizable Variables
- `num_of_rotors`: Number of rotors in use.
- `len_of_cluster`: Number of characters in each cluster during encryption.
- `valid_roman_numerals`: Set of valid Roman numerals for rotor order.

## Input Validation
- **Rotor Order:** Must be a number Roman numerals specified by `num_of_rotors` representing the rotor order.
- **Plugboard Sequence:** Consists of letter pairs separated by spaces, with a maximum of 13 swaps.
- **Ring Settings and Starting Positions:** Accepts numbers in range 1-26 or numbers separated by spaces, either of length specified by `num_of_rotors`.
- **Text:** For decryption, the pattern must match the specified format.

## Notes
- The sequence 'HRL' in example output represents a null sequence for the space ' ' character.
- Encrypted output contains letters in groups of four, and decrypted messages contain letters and special characters in word groups.
- This Emulator is not an exact replica of the one used in world war two. This emulator is a model of the **#Terminal Community**.
- `_decrypt` method inside the `EnigmaEmulator` class might not always work as expected.

Feel free to contribute or report issues on [GitHub](https://github.com/Genesis-js/Cryptography)
