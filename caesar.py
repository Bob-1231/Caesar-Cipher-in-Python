def caesar_cipher(message, shift): 
    global encrypted_message
    encrypted_message = ""
    for character in message: 
        if character == ' ': 
            encrypted_message += ' ' 
        elif  character.isupper(): 
            encrypted_message += chr((ord(character) + shift - 65) % 26 + 65) 
        else: 
            encrypted_message += chr((ord(character) + shift - 97) % 26 + 97) 
    return encrypted_message 

def decrypt_caesar(encrypted_message, key): 
    plaintext = "" 
  
    for char in encrypted_message: 
        if char == ' ': 
            plaintext += ' '
        elif  char.isupper(): 
            plaintext += chr((ord(char) - key - 65) % 26 + 65) 
        else: 
            plaintext += chr((ord(char) - key - 97) % 26 + 97) 
  
    return plaintext 

if __name__ == "__main__": 
    message = input("Please input your message: ")
    shift = 2
    print("Encrypted Message is: " + caesar_cipher(message, shift))
    print("Plaintext:", decrypt_caesar(encrypted_message, shift))