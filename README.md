111111111111111111111111111
#include <stdio.h>

int main()
{
    char *str = "Hello World";

    printf("Original String:%s\n", str);

    printf("After XOR with 0:");

    for (int i = 0; str[i] != '\0'; i++)
    {
        char ch = str[i] ^ 0;
        printf("%c", ch);
    }

    return 0;
}

2222222222222222222222222222
#include <stdio.h>

int main()
{
    char *str = "Hello World";

    printf("Original String: %s\n", str);

    // AND operation with 127
    printf("\nAfter AND with 127: ");
    for (int i = 0; str[i] != '\0'; i++)
    {
        printf("%c", str[i] & 127);
    }

    // XOR operation with 127
    printf("\nAfter XOR with 127: ");
    for (int i = 0; str[i] != '\0'; i++)
    {
        printf("%c", str[i] ^ 127);
    }

    // OR operation with 127
    printf("\nAfter OR with 127: ");
    for (int i = 0; str[i] != '\0'; i++)
    {
        printf("%c", str[i] | 127);
    }

    printf("\n");

    return 0;
}

333333333333333333333
import java.util.Scanner;

public class Hill {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[][] key = {{3, 3}, {2, 5}};
        int[][] inverse = {{15, 17}, {20, 9}};

        System.out.print("Enter plaintext: ");
        String text = sc.nextLine().toUpperCase().replace(" ", "");

        // Add X if length is odd
        if (text.length() % 2 != 0) {
            text += "X";
        }

        String encrypted = "";
        String decrypted = "";

        // Encryption
        for (int i = 0; i < text.length(); i += 2) {
            int a = text.charAt(i) - 'A';
            int b = text.charAt(i + 1) - 'A';

            int c1 = (3 * a + 3 * b) % 26;
            int c2 = (2 * a + 5 * b) % 26;

            encrypted += (char) (c1 + 'A');
            encrypted += (char) (c2 + 'A');
        }

        // Decryption
        for (int i = 0; i < encrypted.length(); i += 2) {
            int a = encrypted.charAt(i) - 'A';
            int b = encrypted.charAt(i + 1) - 'A';

            int c1 = (15 * a + 17 * b) % 26;
            int c2 = (20 * a + 9 * b) % 26;

            decrypted += (char) (c1 + 'A');
            decrypted += (char) (c2 + 'A');
        }

        System.out.println("Prepared plaintext: " + text);
        System.out.println("Encrypted text: " + encrypted);
        System.out.println("Decrypted text: " + decrypted);

        sc.close();
    }
}

4444444444444444444444
import java.util.Scanner;

public class Playfair {
    static char[][] mat = new char[5][5];

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter keyword: ");
        String key = sc.nextLine().toUpperCase().replace('J', 'I');

        System.out.print("Enter plaintext: ");
        String text = sc.nextLine().toUpperCase().replace('J', 'I');

        // Create key matrix
        String s = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ";
        String unique = "";

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'A' && c <= 'Z' && unique.indexOf(c) == -1)
                unique += c;
        }

        for (int i = 0; i < 25; i++)
            mat[i / 5][i % 5] = unique.charAt(i);

        // Prepare plaintext pairs
        String p = "";
        for (int i = 0; i < text.length(); i++) {
            char a = text.charAt(i);
            p += a;

            if (i + 1 < text.length()) {
                if (a == text.charAt(i + 1))
                    p += 'X';
                else
                    p += text.charAt(++i);
            } else {
                p += 'X';
            }
        }

        // Encryption and decryption
        String enc = "", dec = "";

        for (int i = 0; i < p.length(); i += 2) {
            char a = p.charAt(i), b = p.charAt(i + 1);
            int r1 = 0, c1 = 0, r2 = 0, c2 = 0;

            for (int r = 0; r < 5; r++)
                for (int c = 0; c < 5; c++) {
                    if (mat[r][c] == a) { r1 = r; c1 = c; }
                    if (mat[r][c] == b) { r2 = r; c2 = c; }
                }

            if (r1 == r2) {
                enc += mat[r1][(c1 + 1) % 5];
                enc += mat[r2][(c2 + 1) % 5];
                dec += mat[r1][(c1 + 4) % 5];
                dec += mat[r2][(c2 + 4) % 5];
            } else if (c1 == c2) {
                enc += mat[(r1 + 1) % 5][c1];
                enc += mat[(r2 + 1) % 5][c2];
                dec += mat[(r1 + 4) % 5][c1];
                dec += mat[(r2 + 4) % 5][c2];
            } else {
                enc += mat[r1][c2];
                enc += mat[r2][c1];
                dec += mat[r1][c2];
                dec += mat[r2][c1];
            }
        }

        System.out.println("\nKey Matrix:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++)
                System.out.print(mat[i][j] + " ");
            System.out.println();
        }

        System.out.println("Prepared Text: " + p);
        System.out.println("Encrypted Text: " + enc);
        System.out.println("Decrypted Text: " + dec);

        sc.close();
    }
}

555555555555555555555
import java.util.Scanner;

public class Hill {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[][] key = {{3, 3}, {2, 5}};
        int[][] inverse = {{15, 17}, {20, 9}};

        System.out.print("Enter plaintext: ");
        String text = sc.nextLine().toUpperCase().replace(" ", "");

        // Add X if length is odd
        if (text.length() % 2 != 0) {
            text += "X";
        }

        String encrypted = "";
        String decrypted = "";

        // Encryption
        for (int i = 0; i < text.length(); i += 2) {
            int a = text.charAt(i) - 'A';
            int b = text.charAt(i + 1) - 'A';

            int c1 = (3 * a + 3 * b) % 26;
            int c2 = (2 * a + 5 * b) % 26;

            encrypted += (char) (c1 + 'A');
            encrypted += (char) (c2 + 'A');
        }

        // Decryption
        for (int i = 0; i < encrypted.length(); i += 2) {
            int a = encrypted.charAt(i) - 'A';
            int b = encrypted.charAt(i + 1) - 'A';

            int c1 = (15 * a + 17 * b) % 26;
            int c2 = (20 * a + 9 * b) % 26;

            decrypted += (char) (c1 + 'A');
            decrypted += (char) (c2 + 'A');
        }

        System.out.println("Prepared plaintext: " + text);
        System.out.println("Encrypted text: " + encrypted);
        System.out.println("Decrypted text: " + decrypted);

        sc.close();
    }
}

66666666666666666666666666666666666
import javax.crypto.*;
import java.util.Base64;
import java.util.Scanner;

public class DESExample {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        // Generate DES key
        KeyGenerator kg = KeyGenerator.getInstance("DES");
        SecretKey key = kg.generateKey();

        // Create Cipher object
        Cipher cipher = Cipher.getInstance("DES");

        System.out.print("Enter Plain Text: ");
        String message = sc.nextLine();

        // Encryption
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encrypted = cipher.doFinal(message.getBytes());

        String enc = Base64.getEncoder().encodeToString(encrypted);

        System.out.println("Original Message: " + message);
        System.out.println("Encrypted Message: " + enc);

        // Decryption
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decrypted = cipher.doFinal(Base64.getDecoder().decode(enc));

        System.out.println("Decrypted Message: " + new String(decrypted));

        sc.close();
    }
}
7777777777777777777777
import javax.crypto.*;
import java.util.Base64;
import java.util.Scanner;

public class BlowfishExample {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        // Generate Blowfish key
        KeyGenerator kg = KeyGenerator.getInstance("Blowfish");
        kg.init(128);
        SecretKey key = kg.generateKey();

        Cipher cipher = Cipher.getInstance("Blowfish");

        System.out.print("Enter Plain Text: ");
        String message = sc.nextLine();

        // Encryption
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encrypted = cipher.doFinal(message.getBytes());

        String enc = Base64.getEncoder().encodeToString(encrypted);

        System.out.println("Original Message: " + message);
        System.out.println("Encrypted Message: " + enc);

        // Decryption
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decrypted = cipher.doFinal(Base64.getDecoder().decode(enc));

        System.out.println("Decrypted Message: " + new String(decrypted));

        sc.close();
    }
}

8888888888888888888
import javax.crypto.*;
import java.util.Base64;
import java.util.Scanner;

public class RijndaelExample {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        // Generate AES key
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(128);
        SecretKey key = kg.generateKey();

        Cipher cipher = Cipher.getInstance("AES");

        System.out.print("Enter Plain Text: ");
        String message = sc.nextLine();

        // Encryption
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encrypted = cipher.doFinal(message.getBytes());

        String enc = Base64.getEncoder().encodeToString(encrypted);

        System.out.println("Original Message: " + message);
        System.out.println("Encrypted Message: " + enc);

        // Decryption
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decrypted = cipher.doFinal(Base64.getDecoder().decode(enc));

        System.out.println("Decrypted Message: " + new String(decrypted));

        sc.close();
    }
}

999999999999999999999
import java.util.Scanner;

public class rsa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter p: ");
        int p = sc.nextInt();

        System.out.print("Enter q: ");
        int q = sc.nextInt();

        int n = p * q;
        int phi = (p - 1) * (q - 1);

        System.out.print("Enter e: ");
        int e = sc.nextInt();

        // Calculate private key d
        int d = 1;
        while ((d * e) % phi != 1) {
            d++;
        }

        System.out.print("Enter message: ");
        int m = sc.nextInt();

        // Encryption
        int c = 1;
        for (int i = 0; i < e; i++) {
            c = (c * m) % n;
        }

        // Decryption
        int decrypted = 1;
        for (int i = 0; i < d; i++) {
            decrypted = (decrypted * c) % n;
        }

        System.out.println("n = " + n);
        System.out.println("phi(n) = " + phi);
        System.out.println("Public Key: (" + e + ", " + n + ")");
        System.out.println("Private Key: (" + d + ", " + n + ")");
        System.out.println("Encrypted Message: " + c);
        System.out.println("Decrypted Message: " + decrypted);

        sc.close();
    }
}
Enter p: 3
Enter q: 11
Enter e: 3
Enter message: 4

n = 33
phi(n) = 20
Public Key: (3, 33)
Private Key: (7, 33)
Encrypted Message: 31
Decrypted Message: 4

1010101011010101010101
import java.util.Scanner;

public class DiffieHellman {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int p = 23, g = 5;

        System.out.print("Enter private key of Alice: ");
        int a = sc.nextInt();

        System.out.print("Enter private key of Bob: ");
        int b = sc.nextInt();

        // Generate public keys
        int Pa = (int) (Math.pow(g, a) % p);
        int Pb = (int) (Math.pow(g, b) % p);

        // Generate shared keys
        int Ka = (int) (Math.pow(Pb, a) % p);
        int Kb = (int) (Math.pow(Pa, b) % p);

        System.out.println("Public prime: " + p);
        System.out.println("Public generator: " + g);
        System.out.println("Alice public key: " + Pa);
        System.out.println("Bob public key: " + Pb);
        System.out.println("Shared key of Alice: " + Ka);
        System.out.println("Shared key of Bob: " + Kb);

        if (Ka == Kb) {
            System.out.println("Key exchange successful!");
        } else {
            System.out.println("Key exchange failed!");
        }

        sc.close();
    }
}
Enter private key of Alice: 6
Enter private key of Bob: 15

Public prime: 23
Public generator: 5
Alice public key: 8
Bob public key: 19
Shared key of Alice: 2
Shared key of Bob: 2
Key exchange successful!

1111111111111111111111111111111
import java.security.MessageDigest;
import java.util.Scanner;

public class SHA1Example {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the text: ");
        String message = sc.nextLine();

        // Generate SHA-1 hash
        MessageDigest md = MessageDigest.getInstance("SHA-1");
        byte[] digest = md.digest(message.getBytes());

        // Convert byte array into hexadecimal
        StringBuilder result = new StringBuilder();

        for (byte b : digest) {
            result.append(String.format("%02x", b & 0xff));
        }

        System.out.println("Original Message: " + message);
        System.out.println("SHA-1 Message Digest: " + result);

        sc.close();
    }
}

1212121212121212
import java.security.MessageDigest;
import java.util.Scanner;

public class MD5Example {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the text: ");
        String message = sc.nextLine();

        // Generate MD5 hash
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digest = md.digest(message.getBytes());

        // Convert bytes into hexadecimal
        StringBuilder result = new StringBuilder();

        for (byte b : digest) {
            result.append(String.format("%02x", b & 0xff));
        }

        System.out.println("Original Message: " + message);
        System.out.println("MD5 Message Digest: " + result);

        sc.close();
    }
}
