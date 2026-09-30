#BO, 6th, cipher

#ask user for information
encrypt_decrypt = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
message = input("Enter a message to encrypt: ")
if message.isnumeric():
    print("Please input words.")
shift = int(input("Enter the amount you want to shift: "))

def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Determine the starting point based on case
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_message += shifted_char
        else:
            encrypted_message += char  # Non-alphabetic characters are not changed
    return encrypted_message

print(f"Your encrypted message is: {encrypt(message, shift)}")