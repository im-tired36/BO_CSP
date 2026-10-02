#BO, 6th, caesar cipher

#ask user for information
encrypt_decrypt = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
message = input("Enter a message to encrypt: ")
while message.isnumeric():
    print("Please input words.")
    message = input("Enter a message to encrypt: ")
shift = int(input("Enter the amount you want to shift: "))

def caesar_shift(message, shift):
    result = ""
    
    if encrypt_decrypt == "E":
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
    else:
        if encrypt_decrypt == "D":
            for char in message:
                if char.isalpha():
                    if char.isupper():
                        shifted = (ord(char) - ord("A") - shift) % 26
                        decrypted = chr(shifted + ord("A"))
                        result += decrypted
                    else:
                        if char.islower():
                            shifted = (ord(char) - ord("a") - shift) % 26
                            decrypted = chr(shifted + ord("a"))
                            result += decrypted
                else:
                    result += char
    return result

result = caesar_shift(message, shift)
print(result)
       
