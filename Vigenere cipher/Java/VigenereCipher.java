import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class VigenereCipher {
    public static void main(String[] args) {
        System.out.println("Java program for working with the Vigenere Cipher. (Encrypter and Decrypter)\n");

        // Declaring data to be used for encryption and decryption.
        char[] alphabets = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        Map<Character, Integer> alphaIndex = new HashMap<>();
        for (int i = 0; i < alphabets.length; i++) {
            alphaIndex.put(alphabets[i], i);
        }

        // Handling input for the Cipher key. Note minus sign before key for decryption and plus sign for encryption.
        String key;
        boolean decrypt = false;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Key (Enter a minus sign before key for decryption and plus sign for encryption e.g +key, -key): ");
            key = scanner.nextLine();
            boolean valid = key.length() > 1 && (key.charAt(0) == '+' || key.charAt(0) == '-');
            for (int i = 1; i < key.length(); i++) {
                if (!Character.isLetter(key.charAt(i))) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                decrypt = key.charAt(0) == '-';
                break;
            }
            System.out.println("Invalid Key");
        }

        // Collecting string to be decrypted or encrypted.
        if (decrypt) {
            System.out.print("Encrypted Text: ");
        } else {
            System.out.print("Plain Text: ");
        }
        String plainText = scanner.nextLine();

        // Working the magic.
        int keyLength = key.length() - 1;
        int counter = 1;
        for (char c : plainText.toCharArray()) {
            if (Character.isLetter(c)) {
                boolean isUppercase = Character.isUpperCase(c);
                int newIdx = (alphaIndex.get(Character.toLowerCase(c)) + alphaIndex.get(Character.toLowerCase(key.charAt(counter)))) % 26;
                int decryptIdx = (alphaIndex.get(Character.toLowerCase(c)) - alphaIndex.get(Character.toLowerCase(key.charAt(counter))) + 26) % 26;
                int newIndex = decrypt ? decryptIdx : newIdx;
                counter = 1 + ((counter + 1) % keyLength);
                System.out.print(isUppercase ? Character.toUpperCase(alphabets[newIndex]) : alphabets[newIndex]);
            } else {
                System.out.print(c);
            }
        }

        System.out.println("\n[Program finished]");
    }
}