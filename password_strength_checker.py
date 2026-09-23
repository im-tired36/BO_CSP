#BO, 6th, Password Strenth Checker

password = input("What is your password:")
length = False
uppercase = False
lowercase = False
number = False
symbol = False

if len(password) >= 8:
    length = True
else:
    print(f"At least 8 characters: {length}")
print(f"At least 8 character: {length}")

for letter in password:
    if letter.isupper():
        uppercase = True
print(f"Has an uppercase letter: {uppercase}")

for letter in password:
    if letter.islower():
        lowercase = True
print(f"Has a lowercase letter: {lowercase}")

for letter in password:
    if letter.isnumeric():
        number = True
print(f"Has a number: {number}")

for letter in "!@#$%^&*();:?/<>,.`~-_=+":
    symbol = True
