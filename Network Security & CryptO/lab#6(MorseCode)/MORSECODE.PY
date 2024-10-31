print('-------------------------MORSE CODE PROGRAM------------------------------')
userinput=input("Enter your text : ").upper()
key={
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 
    'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..'
    }          
def encrypt(msg,key):
    encmsg=""
    for i in msg:
        encmsg+=key[i]+ " "
    
    return encmsg

def decrypt(msg,key):
    decmsg=""
    tempchar=""
    for i in msg:
        if i!= " ":
           tempchar+=i
        else:
           decmsg+=list(key.keys())[list(key.values()).index(tempchar)]
           tempchar=""
    return decmsg
encrypt_txt=encrypt(userinput,key)
decrypt_txt=decrypt(encrypt_txt,key)
print("\nYour Encrypted text is :** ",encrypt_txt)
print("\nYour Decrypted text is :- ",decrypt_txt)
print("\n \t\t ******************* \t\t \n")