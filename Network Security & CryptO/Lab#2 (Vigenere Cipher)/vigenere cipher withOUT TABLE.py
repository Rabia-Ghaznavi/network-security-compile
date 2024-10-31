print('--------------------------VIGENERE CIPHER WITHOUT TABLE------------------------------')
def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using Vigenère cipher"""
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using Vigenère cipher"""
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    encrypted_text = vigenere_encrypt(plaintext, key)
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("\nPlaintext:", plaintext)
    print("Key:", key)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
