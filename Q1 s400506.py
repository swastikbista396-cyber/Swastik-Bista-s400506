def encrypt_character(char, shift1, shift2):
    """
    Encrypt a single character based on given rules.
    """

    # Lowercase letters
    if char.islower():
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:  # n-z
            shift = shift1 + shift2
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

    # Uppercase letters
    elif char.isupper():
        if 'A' <= char <= 'M':
            return chr((ord(char) - ord('A') - shift1) % 26 + ord('A'))
        else:  # N-Z
            return chr((ord(char) - ord('A') + (shift2 ** 2)) % 26 + ord('A'))

    # Other characters remain unchanged
    return char


def decrypt_character(char, shift1, shift2):
    """
    Reverse the encryption logic.
    """

    if char.islower():
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            shift = shift1 + shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

    elif char.isupper():
        if 'A' <= char <= 'M':
            return chr((ord(char) - ord('A') + shift1) % 26 + ord('A'))
        else:
            return chr((ord(char) - ord('A') - (shift2 ** 2)) % 26 + ord('A'))

    return char


def encrypt_file(shift1, shift2):
    """Read raw_text.txt and write encrypted_text.txt"""

    with open("raw_text.txt", "r") as file:
        text = file.read()

    encrypted_text = ""
    for char in text:
        encrypted_text += encrypt_character(char, shift1, shift2)

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)


def decrypt_file(shift1, shift2):
    """Read encrypted_text.txt and write decrypted_text.txt"""

    with open("encrypted_text.txt", "r") as file:
        text = file.read()

    decrypted_text = ""
    for char in text:
        decrypted_text += decrypt_character(char, shift1, shift2)

    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)


def verify_decryption():
    """Compare original and decrypted files"""

    with open("raw_text.txt", "r") as file:
        original = file.read()

    with open("decrypted_text.txt", "r") as file:
        decrypted = file.read()

    if original == decrypted:
        print("Verification: SUCCESS")
    else:
        print("Verification: FAILED")


def main():
    """Main program execution"""

    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify_decryption()


if __name__ == "__main__":
    main()