print('--------------------------RAIL FENCE PROGRAM------------------------------')
def main():
    action = input("Choose action (1 for encryption, 2 for decryption): ").strip()
    text = input("Enter your text: ")
    key = int(input("Enter the key (number of rails): "))

    if action == '1':
        processed_text = cipher(text, key)
        print(f"\nCiphered Text: {processed_text}")
    elif action == '2':
        processed_text = decipher(text, key)
        print(f"\nDeciphered Text: {processed_text}")
    else:
        print("\nInvalid action selected.")

def cipher(clear_text, key):
    if key == 1:
        return clear_text
    result = []
    cycle_len = 2 * key - 2

    for i in range(key):
        for j in range(i, len(clear_text), cycle_len):
            result.append(clear_text[j])
            if i != 0 and i != key - 1 and j + cycle_len - 2*i < len(clear_text):
                result.append(clear_text[j + cycle_len - 2*i])

    return ''.join(result)

def decipher(cipher_text, key):
    if key == 1:
        return cipher_text

    n = len(cipher_text)
    matrix = [''] * n
    index = 0
    cycle_len = 2 * key - 2

    for r in range(key):
        step = cycle_len - 2 * r
        i = r
        while i < n:
            matrix[i] = cipher_text[index]
            index += 1
            i += cycle_len
            if r != 0 and r != key - 1 and i < n:
                matrix[i] = cipher_text[index]
                index += 1
                i += step

    return ''.join(matrix)

if __name__ == "__main__":
    main()