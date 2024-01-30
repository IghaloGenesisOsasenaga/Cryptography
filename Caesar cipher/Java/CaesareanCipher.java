import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CaesareanCipher {
    public static void main(String[] args) {
        System.out.println("Java program for working with the Caesarean Cipher. (Encrypter and Decrypter)\n");

        // Declaring data to be used for encryption and decryption.
        char[] alphabets = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        Map<Character, Integer> alphaIndex = new HashMap<>();
        for (int i = 0; i < alphabets.length; i++) {
            alphaIndex.put(alphabets[i], i);
        }

        // Handling input for the Cipher shift. Note negative shift for decryption and positive for encryption.
        int shift = 0;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Shift (Enter a negative integer for decryption): ");
            String inputShift = scanner.nextLine().replace(" ", "");
            boolean valid = true;
            for (char c : inputShift.toCharArray()) {
                if (!Character.isDigit(c) && c != '-') {
                    valid = false;
                    break;
                }
            }

            if (inputShift.contains("-")) {
                int num_of_neg_sign = (int) inputShift.chars().filter(ch -> ch == '-').count();
                if (num_of_neg_sign > 1 || inputShift.charAt(0) != '-') {
                    valid = false;
                }
            }

            if (valid && !inputShift.equals("")) {
                shift = Integer.parseInt(inputShift) % 26;
                break;
            } else {
                System.out.println("Enter a valid integer");
            }
        }

        // Collecting string to be decrypted or encrypted.
        System.out.print(shift < 0 ? "Encrypted Text: " : "Plain Text: ");
        String plainText = scanner.nextLine();

        // Working the magic.
        StringBuilder result = new StringBuilder();
        for (char c : plainText.toCharArray()) {
            if (Character.isAlphabetic(c)) {
                boolean isUppercase = Character.isUpperCase(c);
                int newIndex = (alphaIndex.get(Character.toLowerCase(c)) + shift + 26) % 26;
                result.append(isUppercase ? Character.toUpperCase(alphabets[newIndex]) : alphabets[newIndex]);
            } else {
                result.append(c);
            }
        }

        System.out.println(result.toString() + "\n[Program finished]");
    }
}