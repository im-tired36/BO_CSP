#BO, 6th, cipher

#ask user for information
encrypt_decrypt = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
message = input("Enter a message to encrypt: ")
if message.isnumeric():
    print("Please input words.")
shift = int(input("Enter the amount you want to shift: "))

def encryptdecrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message
