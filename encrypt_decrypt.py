def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryption/Decryption Tool ===")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()

    if choice not in ['E', 'D']:
        print("Invalid option. Exiting.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift number (e.g., 3): "))
    except ValueError:
        print("Invalid shift number. Exiting.")
        return

    if choice == 'E':
        result = caesar_encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = caesar_decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()