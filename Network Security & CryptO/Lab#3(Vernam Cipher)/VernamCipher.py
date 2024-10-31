print('--------------------------VERNAM CIPHER PROGRAM------------------------------')
def char_to_num(char):
    """Convert character to number where 'a'/'A' = 0, 'b'/'B' = 1, ..., 'z'/'Z' = 25."""
    if 'a' <= char <= 'z':
        return ord(char) - ord('a')
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    else:
        return None

def num_to_char(num):
    """Convert number to character where 0 = 'a', 1 = 'b', ..., 25 = 'z'."""
    return chr(num + ord('a'))

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the Vernam cipher."""
    plaintext = ""  
    print("\n *****VERNAM CIPHER DECRYPTION*****")
    print("\nSubtraction Result (numbers):")
    for c, k in zip(ciphertext, key):  
        ciphertext_num = char_to_num(c)  
        key_num = char_to_num(k) 
        if ciphertext_num is not None and key_num is not None:  
            print(f"{ciphertext_num} (ciphertext) - {key_num} (key) =", end=" ") 
            subtracted_num = (ciphertext_num - key_num)
            print(subtracted_num, end=", ") 
            if subtracted_num < 0:  
                subtracted_num += 26  
                print(f"(Adjusted by adding 26: {subtracted_num})", end=", ")
            decrypted_char = num_to_char(subtracted_num) 
            plaintext += decrypted_char  
            print(decrypted_char)  
    return plaintext  


def main():
    print("\n*****VERNAM CIPHER ENCRYPTION*****")
    plaintext = input("Enter the plaintext: ").lower()
    
    # Count non-space characters in plaintext
    plaintext_count = sum(1 for char in plaintext if char != ' ')
    
   
    while True:
        key = input(f"Enter the key ({plaintext_count} characters): ").lower().replace(" ", "")
        if len(key) != plaintext_count:
            print("Error: Key length must match plaintext length (excluding spaces).")
        else:
            break

    print("\nPlaintext (numbers):")
    plaintext_nums = []
    for char in plaintext:
        if char != ' ':
            num = char_to_num(char)
            if num is not None:
                print(f"{char} -> {num}")
                plaintext_nums.append(num)

    print("\nKey (numbers):")
    key_nums = []
    for char in key:
        num = char_to_num(char)
        if num is not None:
            print(f"{char} -> {num}")
            key_nums.append(num)

    # Perform addition of corresponding numbers in plaintext and key
    print("\nAddition Result (numbers):")
    result_nums = [(p + k) for p, k in zip(plaintext_nums, key_nums)]
    for num in result_nums:
        print(num)

    # Subtract values greater than or equal to 26 by 26
    print("\nAdjusted Result (numbers):")
    adjusted_nums = []
    for num in result_nums:
        if num >= 26:
            adjusted_num = num - 26
            adjusted_nums.append(adjusted_num)
            print(adjusted_num)
        else:
            adjusted_nums.append(num)
            print(num)

    # Convert numbers back to characters
    print("\nCiphertext (characters):")
    result_chars = [num_to_char(num) for num in adjusted_nums]
    for char in result_chars:
        print(char)

    decrypted_text = decrypt(result_chars, key)
    print("\nDecrypted text:", decrypted_text)

if __name__ == "__main__":
    main()

