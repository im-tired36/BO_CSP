def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Choose the correct alphabet base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')

            # Shift the letter and wrap around the alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Keep spaces, numbers, and punctuation unchanged
            result += char

    return result


print("=== Caesar Cipher ===")
message = input("Enter your message: ")
shift = int(input("Enter shift amount (0-25): "))
mode = input("Encrypt or decrypt? ").lower().strip()

if mode in ("encrypt", "decrypt"):
    print("Result:", caesar_cipher(message, shift, mode))
else:
    print("Invalid mode! Choose encrypt or decrypt.")