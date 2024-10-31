print('                                ')
print('--------------------------CAESAR CIPHER PROGRAM------------------------------')
print('                                ')

#Creating an ENCRYPTION Function
def encrypt(text,shift): #Passsing arguments 
    result = "" # initialize an empty string
    for char in text :
        if char.isupper(): #set condition to chk
            result+= chr((ord(char) + shift -65 )% 26 + 65) #Formula for upper case 
        elif char.islower(): #for lower case
            result+= chr((ord(char)  + shift -95)% 26 + 95) # for Lowercase
        else :
          result += char #for space
    return result #return encrypt txt 

def decrypt(text,shift):
    result = ""

    for char in text :
        if char.isupper():
            result+= chr((ord(char)- shift -65 ) % 26 + 65 )
        elif char.islower():
            result+= chr((ord(char)- shift - 97) % 26 + 97 )

        else :
            result += char

    return result

def get_input(): # create a fun
    text = input("Enter Text:  ")
    shift = int(input("Enter Shift Value  : "))
    return text, shift

while True: # keep ask the option until user exit it
   print ("What Do You Want: ")
   action = input("Enter 'E' for Encryption, 'D' for Decryption, or 'X' to Exit: ").lower()

   if action == 'x' :
       break 
   
   elif action =='e' : #ENC
       text, shift = get_input() #gwt shift and text from user
       encrypted_text = encrypt(text,shift)
       print("Encrypted Text:", encrypted_text)
   elif action == 'd': #DEC
       text , shift = get_input()
       decrypted_text =decrypt(text,shift)
       print("Decrypted Text:", decrypted_text)
   else :
       print("Invalid input. Please enter 'E' for Encryption, 'D' for Decryption, or 'X' to Exit.")
