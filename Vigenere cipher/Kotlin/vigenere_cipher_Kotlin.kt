fun main() {
    println("Kotlin program for working with the Vigenere Cipher. (Encrypter and Decrypter)\n")

    // Declaring data to be used for encryption and decryption.
    val alphabets = ('a'..'z').toList()
    val alphaIndex = alphabets.withIndex().associate { it.value to it.index }

    // Handling input for the Cipher key. Note minus sign before key for decryption and plus sign for encryption.
    var key: String
    var decrypt = false
    while (true) {
        print("Key (Enter a minus sign before key for decryption and plus sign for encryption e.g +key, -key): ")
        key = readLine() ?: ""
        val valid = key.length > 1 && (key[0] == '+' || key[0] == '-') && key.substring(1).all { it.isLetter() }
        if (valid) {
            decrypt = key[0] == '-'
            break
        }
        println("Invalid Key")
    }

    // Collecting string to be decrypted or encrypted.
    if (decrypt) {
        print("Encrypted Text: ")
    } else {
        print("Plain Text: ")
    }
    val plainText = readLine() ?: ""

    // Working the magic.
    val keyLength = key.length - 1
    var counter = 1
    for (char in plainText) {
        if (char.isLetter()) {
            val isUppercase = char.isUpperCase()
            val encryptIdx = (alphaIndex[char.toLowerCase()]!! + alphaIndex[key[counter].toLowerCase()]!!) % 26
            val decryptIdx = (alphaIndex[char.toLowerCase()]!! - alphaIndex[key[counter].toLowerCase()]!! + 26) % 26
            val newIndex = if (decrypt) decryptIdx else encryptIdx
            counter = 1 + ((counter + 1) % keyLength)
            print(if (isUppercase) alphabets[newIndex].toUpperCase() else alphabets[newIndex])
        } else {
            print(char)
        }
    }

    println("\n[Program finished]")
}