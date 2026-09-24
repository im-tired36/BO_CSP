#BO, 6th, Password Strenth Checker

password = input("What is your password:")
length = False
uppercase = False
lowercase = False
number = False
symbol = False
count = 0
strength = "weak"

if len(password) >= 8:
    length = True
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

for letter in password:
    if letter in "!@#$%^&*();:?/<>,.`~-_=+":
         symbol = True
print(f"Has a symbol: {symbol}")

if length == True:
    count = count + 1 
if uppercase == True:
    count = count + 1 
if lowercase == True:
    count = count + 1 
if number == True:
    count = count + 1 
if symbol == True:
    count = count + 1 

if count == 5:
    strength = "strong"
if count <= 4:
    strength = "meduim"
if count < 3:
    strength = "weak"

print(f"You have a {strength} password.")
print(f"You have done {count}/5.")
print("If you don't have a 5/5, you should check if you have a uppercase letter, lowercase letter, a number, and a symbol.")