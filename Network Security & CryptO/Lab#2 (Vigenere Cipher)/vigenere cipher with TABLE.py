print('--------------------------VIGENERE CIPHER WITH TABLE------------------------------')

def generate_vigenere_table():
    """Generate Vigenère table"""
    table = [] 
    for i in range(26):
        row = [chr((i + j) % 26 + 65) for j in range(26)]
        table.append(row)
    return table

def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using Vigenère cipher"""
    plaintext = plaintext.upper()
    key = key.upper()
    table = generate_vigenere_table()
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            row = ord(key[key_index % len(key)]) - 65
            col = ord(char) - 65
            ciphertext += table[row][col]
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using Vigenère cipher"""
    ciphertext = ciphertext.upper()
    key = key.upper()
    table = generate_vigenere_table()
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            row = ord(key[key_index % len(key)]) - 65
            col = table[row].index(char)
            plaintext += chr(col + 65)
            key_index += 1
        else:
            plaintext += char
    return plaintext

def print_vigenere_table():
    """Print Vigenère table"""
    table = generate_vigenere_table()
    print("    ")
    print("          Vigenere Table:")
    for row in table:
        print(' '.join(row))

if __name__ == "__main__":
    print_vigenere_table()
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    encrypted_text = vigenere_encrypt(plaintext, key)
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("\nPlaintext:", plaintext)
    print("Key:", key)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
