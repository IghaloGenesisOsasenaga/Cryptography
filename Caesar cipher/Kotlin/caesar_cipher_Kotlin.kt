fun main() {
    println("Kotlin program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n")

    // Declaring data to be used for encryption and decryption.
    val alphabets = ('a'..'z').toList()
    val alphaIndex = alphabets.withIndex().associate { it.value to it.index }

    // Handling input for the Cipher shift. Note negative shift for decryption and positive for encryption.
    var shift: Int
    while (true) {
        print("Shift Enter a negative integer for decryption): ")
        val input = readLine()?.replace(" ", "")
        val isValid = input?.let {
            it.all { char -> char.isDigit() || char == '-' } &&
                    (!input.contains('-') ||
                    (input.count { char -> char == '-' } <= 1 && input.first() == '-'))
        } ?: false

        if (isValid && !input.isNullOrBlank()) {
            shift = input.toInt() % 26
            break
        } else {
            println("Enter a valid integer")
        }
    }

    // Collecting string to be decrypted or encrypted.
    print(if (shift < 0) "Encrypted Text: " else "Plain Text: ")
    val plainText = readLine()

    // Working the magic.
    plainText?.forEach { char ->
        if (char.isLetter()) {
            val isUppercase = char.isUpperCase()
            val newIdx = (alphaIndex[char.toLowerCase()]!! + shift + 26) % 26
            print(if (isUppercase) alphabets[newIdx].toUpperCase() else alphabets[newIdx])
        } else {
            print(char)
        }
    }

    println("\n[Program finished]")
}