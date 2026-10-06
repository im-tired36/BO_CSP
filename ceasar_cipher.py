#BO, 6th, caesar cipher

#ask user for information
encrypt_decrypt = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
message = input("Enter a message to encrypt/decrypt: ")
while message.isnumeric():
    print("Please input words.")
    message = input("Enter a message to encrypt/decrypt: ")
shift = int(input("Enter the amount you want to shift: "))

def caesar_shift(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                shifted = (ord(char) - ord("A") + shift) % 26
                encrypted = chr(shifted + ord("A"))
                result += encrypted
            else:
                if char.islower():
                    shifted = (ord(char) - ord("a") + shift) % 26
                    encrypted = chr(shifted + ord("a"))
                    result += encrypted
        else:
            result += char
    return result

if encrypt_decrypt == "E":
    result = caesar_shift(message, shift)
    print(result)

if encrypt_decrypt == "D":
    shift = -shift
    result = caesar_shift(message, shift)
    print(result)
